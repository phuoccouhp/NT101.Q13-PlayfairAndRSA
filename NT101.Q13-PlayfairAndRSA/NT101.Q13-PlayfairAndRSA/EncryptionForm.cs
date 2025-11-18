using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Windows.Forms;

namespace NT101.Q13_PlayfairAndRSA // <-- Đảm bảo namespace này khớp với tên Project của bạn
{
    public partial class EncryptionForm : Form
    {
        // Biến lưu trữ khóa RSA
        private RSACryptoServiceProvider rsa;
        private RSAParameters privateKey;
        private RSAParameters publicKey;

        public EncryptionForm()
        {
            // Tải giao diện từ file .designer.cs
            InitializeComponent();

            // Khởi tạo và hiển thị khóa RSA ban đầu
            InitializeRsaKeys();
            DisplayRsaKeys();

            // Cập nhật thanh trạng thái
            mainStatusLabel.Text = "Sẵn sàng. Vui lòng chọn một thuật toán từ menu 'Encrypt/Decrypt'.";
        }

        #region Navigation Logic (Menu)

        // Hàm chung để ẩn tất cả các panel
        private void HideAllPanels()
        {
            panelPlayfair.Visible = false;
            panelRSA.Visible = false;
        }

        private void playfairToolStripMenuItem_Click(object sender, EventArgs e)
        {
            HideAllPanels();
            panelPlayfair.Visible = true;
            mainStatusLabel.Text = "Đã chọn: Encrypt/Decrypt -> Symmetric (classic) -> Playfair";
        }

        private void rsaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            HideAllPanels();
            panelRSA.Visible = true;
            mainStatusLabel.Text = "Đã chọn: Encrypt/Decrypt -> Asymmetric -> RSA";
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        #endregion

        #region Playfair Logic (Không đổi)

        private void BtnPlayfairEncrypt_Click(object sender, EventArgs e)
        {
            try
            {
                string key = txtPlayfairKey.Text;
                string plaintext = txtPlayfairPlaintext.Text;
                txtPlayfairCiphertext.Text = Playfair.Encrypt(plaintext, key);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi khi mã hoá Playfair: " + ex.Message, "Lỗi", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void BtnPlayfairDecrypt_Click(object sender, EventArgs e)
        {
            try
            {
                string key = txtPlayfairKey.Text;
                string ciphertext = txtPlayfairCiphertext.Text;
                txtPlayfairPlaintext.Text = Playfair.Decrypt(ciphertext, key);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi khi giải mã Playfair: " + ex.Message, "Lỗi", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        // Lớp lồng nhau chứa logic Playfair
        private static class Playfair
        {
            private static char[,] keyMatrix;

            private static void GenerateKeyMatrix(string key)
            {
                key = key.ToUpper().Replace("J", "I").Replace(" ", "");
                key = new string(key.ToCharArray().Distinct().ToArray());
                string alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // Không có 'J'
                string keyString = key + alphabet;
                keyString = new string(keyString.ToCharArray().Distinct().ToArray());

                keyMatrix = new char[5, 5];
                int k = 0;
                for (int i = 0; i < 5; i++)
                {
                    for (int j = 0; j < 5; j++)
                    {
                        keyMatrix[i, j] = keyString[k];
                        k++;
                    }
                }
            }

            private static string PrepareText(string text)
            {
                text = text.ToUpper().Replace("J", "I").Replace(" ", "");
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < text.Length; i++)
                {
                    sb.Append(text[i]);
                    if (i + 1 < text.Length && text[i] == text[i + 1])
                    {
                        sb.Append('X');
                    }
                }
                if (sb.Length % 2 != 0)
                {
                    sb.Append('X');
                }
                return sb.ToString();
            }

            private static Point FindPosition(char ch)
            {
                for (int i = 0; i < 5; i++)
                {
                    for (int j = 0; j < 5; j++)
                    {
                        if (keyMatrix[i, j] == ch)
                        {
                            return new Point(j, i); // (x, y) -> (col, row)
                        }
                    }
                }
                return new Point(-1, -1);
            }

            private static string Process(string text, int direction) // 1 for encrypt, -1 for decrypt
            {
                StringBuilder result = new StringBuilder();
                for (int i = 0; i < text.Length; i += 2)
                {
                    char a = text[i];
                    char b = text[i + 1];
                    Point posA = FindPosition(a);
                    Point posB = FindPosition(b);

                    if (posA.Y == posB.Y) // Cùng hàng
                    {
                        result.Append(keyMatrix[posA.Y, (posA.X + direction + 5) % 5]);
                        result.Append(keyMatrix[posB.Y, (posB.X + direction + 5) % 5]);
                    }
                    else if (posA.X == posB.X) // Cùng cột
                    {
                        result.Append(keyMatrix[(posA.Y + direction + 5) % 5, posA.X]);
                        result.Append(keyMatrix[(posB.Y + direction + 5) % 5, posB.X]);
                    }
                    else // Khác hàng, khác cột (hình chữ nhật)
                    {
                        result.Append(keyMatrix[posA.Y, posB.X]);
                        result.Append(keyMatrix[posB.Y, posA.X]);
                    }
                }
                return result.ToString();
            }

            public static string Encrypt(string plaintext, string key)
            {
                if (string.IsNullOrWhiteSpace(key)) throw new ArgumentException("Khóa không được để trống.");
                GenerateKeyMatrix(key);
                string preparedText = PrepareText(plaintext);
                return Process(preparedText, 1);
            }

            public static string Decrypt(string ciphertext, string key)
            {
                if (string.IsNullOrWhiteSpace(key)) throw new ArgumentException("Khóa không được để trống.");
                GenerateKeyMatrix(key);
                string preparedText = ciphertext.ToUpper().Replace(" ", ""); // Giả sử ciphertext đã hợp lệ
                return Process(preparedText, -1);
            }
        }

        #endregion

        #region RSA Logic (Không đổi)

        private void InitializeRsaKeys()
        {
            // Khởi tạo RSA
            rsa = new RSACryptoServiceProvider(2048); // Kích thước khóa 2048 bit
            privateKey = rsa.ExportParameters(true);
            publicKey = rsa.ExportParameters(false);
        }

        private void DisplayRsaKeys()
        {
            // Hiển thị khóa dưới dạng XML string (an toàn để sao chép)
            txtRsaPublicKey.Text = rsa.ToXmlString(false); // false = chỉ public
            txtRsaPrivateKey.Text = rsa.ToXmlString(true);  // true = cả private
        }

        private void BtnRsaGenerateKeys_Click(object sender, EventArgs e)
        {
            try
            {
                InitializeRsaKeys(); // Tạo khóa mới
                DisplayRsaKeys();
                MessageBox.Show("Đã tạo bộ khóa RSA mới (2048-bit).", "Hoàn tất", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi khi tạo khóa RSA: " + ex.Message, "Lỗi", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void BtnRsaEncrypt_Click(object sender, EventArgs e)
        {
            try
            {
                string plaintext = txtRsaPlaintext.Text;
                if (string.IsNullOrEmpty(plaintext))
                {
                    MessageBox.Show("Bản rõ không được để trống.", "Cảnh báo", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }

                byte[] plaintextBytes = Encoding.UTF8.GetBytes(plaintext);

                RSACryptoServiceProvider rsaEncrypt = new RSACryptoServiceProvider();
                rsaEncrypt.FromXmlString(txtRsaPublicKey.Text);

                byte[] ciphertextBytes = rsaEncrypt.Encrypt(plaintextBytes, true);

                txtRsaCiphertext.Text = Convert.ToBase64String(ciphertextBytes);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi khi mã hoá RSA: " + ex.Message, "Lỗi", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void BtnRsaDecrypt_Click(object sender, EventArgs e)
        {
            try
            {
                string ciphertextBase64 = txtRsaCiphertext.Text;
                if (string.IsNullOrEmpty(ciphertextBase64))
                {
                    MessageBox.Show("Bản mã không được để trống.", "Cảnh báo", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }

                byte[] ciphertextBytes = Convert.FromBase64String(ciphertextBase64);

                RSACryptoServiceProvider rsaDecrypt = new RSACryptoServiceProvider();
                rsaDecrypt.FromXmlString(txtRsaPrivateKey.Text);

                byte[] decryptedBytes = rsaDecrypt.Decrypt(ciphertextBytes, true);

                txtRsaPlaintext.Text = Encoding.UTF8.GetString(decryptedBytes);
            }
            catch (CryptographicException)
            {
                MessageBox.Show("Giải mã thất bại. Bản mã hoặc khóa không chính xác, hoặc padding bị lỗi.", "Lỗi Giải mã", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            catch (FormatException)
            {
                MessageBox.Show("Bản mã không phải là một chuỗi Base64 hợp lệ.", "Lỗi Định dạng", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi khi giải mã RSA: " + ex.Message, "Lỗi", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        #endregion
    }
}