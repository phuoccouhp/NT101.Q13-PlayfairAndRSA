namespace NT101.Q13_PlayfairAndRSA // <-- Đảm bảo namespace này khớp với tên Project của bạn
{
    partial class EncryptionForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.mainMenuStrip = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exitToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.encryptDecryptToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.symmetricclassicToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.playfairToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.asymmetricToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.rsaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.panelRSA = new System.Windows.Forms.Panel();
            this.btnRsaDecrypt = new System.Windows.Forms.Button();
            this.btnRsaEncrypt = new System.Windows.Forms.Button();
            this.txtRsaCiphertext = new System.Windows.Forms.TextBox();
            this.lblRsaCiphertext = new System.Windows.Forms.Label();
            this.txtRsaPlaintext = new System.Windows.Forms.TextBox();
            this.lblRsaPlaintext = new System.Windows.Forms.Label();
            this.txtRsaPrivateKey = new System.Windows.Forms.TextBox();
            this.lblRsaPrivateKey = new System.Windows.Forms.Label();
            this.txtRsaPublicKey = new System.Windows.Forms.TextBox();
            this.lblRsaPublicKey = new System.Windows.Forms.Label();
            this.btnRsaGenerateKeys = new System.Windows.Forms.Button();
            this.panelPlayfair = new System.Windows.Forms.Panel();
            this.btnPlayfairDecrypt = new System.Windows.Forms.Button();
            this.btnPlayfairEncrypt = new System.Windows.Forms.Button();
            this.txtPlayfairCiphertext = new System.Windows.Forms.TextBox();
            this.lblPlayfairCiphertext = new System.Windows.Forms.Label();
            this.txtPlayfairPlaintext = new System.Windows.Forms.TextBox();
            this.lblPlayfairPlaintext = new System.Windows.Forms.Label();
            this.txtPlayfairKey = new System.Windows.Forms.TextBox();
            this.lblPlayfairKey = new System.Windows.Forms.Label();
            this.mainToolStrip = new System.Windows.Forms.ToolStrip();
            this.mainStatusStrip = new System.Windows.Forms.StatusStrip();
            this.mainStatusLabel = new System.Windows.Forms.ToolStripStatusLabel();
            this.mainMenuStrip.SuspendLayout();
            this.panelRSA.SuspendLayout();
            this.panelPlayfair.SuspendLayout();
            this.mainStatusStrip.SuspendLayout();
            this.SuspendLayout();
            // 
            // mainMenuStrip
            // 
            this.mainMenuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.encryptDecryptToolStripMenuItem});
            this.mainMenuStrip.Location = new System.Drawing.Point(0, 0);
            this.mainMenuStrip.Name = "mainMenuStrip";
            this.mainMenuStrip.Size = new System.Drawing.Size(784, 24);
            this.mainMenuStrip.TabIndex = 0;
            this.mainMenuStrip.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.exitToolStripMenuItem});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.fileToolStripMenuItem.Text = "File";
            // 
            // exitToolStripMenuItem
            // 
            this.exitToolStripMenuItem.Name = "exitToolStripMenuItem";
            this.exitToolStripMenuItem.Size = new System.Drawing.Size(93, 22);
            this.exitToolStripMenuItem.Text = "Exit";
            this.exitToolStripMenuItem.Click += new System.EventHandler(this.exitToolStripMenuItem_Click);
            // 
            // encryptDecryptToolStripMenuItem
            // 
            this.encryptDecryptToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.symmetricclassicToolStripMenuItem,
            this.asymmetricToolStripMenuItem});
            this.encryptDecryptToolStripMenuItem.Name = "encryptDecryptToolStripMenuItem";
            this.encryptDecryptToolStripMenuItem.Size = new System.Drawing.Size(104, 20);
            this.encryptDecryptToolStripMenuItem.Text = "Encrypt/Decrypt";
            // 
            // symmetricclassicToolStripMenuItem
            // 
            this.symmetricclassicToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.playfairToolStripMenuItem});
            this.symmetricclassicToolStripMenuItem.Name = "symmetricclassicToolStripMenuItem";
            this.symmetricclassicToolStripMenuItem.Size = new System.Drawing.Size(182, 22);
            this.symmetricclassicToolStripMenuItem.Text = "Symmetric (classic)";
            // 
            // playfairToolStripMenuItem
            // 
            this.playfairToolStripMenuItem.Name = "playfairToolStripMenuItem";
            this.playfairToolStripMenuItem.Size = new System.Drawing.Size(113, 22);
            this.playfairToolStripMenuItem.Text = "Playfair";
            this.playfairToolStripMenuItem.Click += new System.EventHandler(this.playfairToolStripMenuItem_Click);
            // 
            // asymmetricToolStripMenuItem
            // 
            this.asymmetricToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.rsaToolStripMenuItem});
            this.asymmetricToolStripMenuItem.Name = "asymmetricToolStripMenuItem";
            this.asymmetricToolStripMenuItem.Size = new System.Drawing.Size(182, 22);
            this.asymmetricToolStripMenuItem.Text = "Asymmetric";
            // 
            // rsaToolStripMenuItem
            // 
            this.rsaToolStripMenuItem.Name = "rsaToolStripMenuItem";
            this.rsaToolStripMenuItem.Size = new System.Drawing.Size(95, 22);
            this.rsaToolStripMenuItem.Text = "RSA";
            this.rsaToolStripMenuItem.Click += new System.EventHandler(this.rsaToolStripMenuItem_Click);
            // 
            // panelRSA
            // 
            this.panelRSA.Controls.Add(this.btnRsaDecrypt);
            this.panelRSA.Controls.Add(this.btnRsaEncrypt);
            this.panelRSA.Controls.Add(this.txtRsaCiphertext);
            this.panelRSA.Controls.Add(this.lblRsaCiphertext);
            this.panelRSA.Controls.Add(this.txtRsaPlaintext);
            this.panelRSA.Controls.Add(this.lblRsaPlaintext);
            this.panelRSA.Controls.Add(this.txtRsaPrivateKey);
            this.panelRSA.Controls.Add(this.lblRsaPrivateKey);
            this.panelRSA.Controls.Add(this.txtRsaPublicKey);
            this.panelRSA.Controls.Add(this.lblRsaPublicKey);
            this.panelRSA.Controls.Add(this.btnRsaGenerateKeys);
            this.panelRSA.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panelRSA.Location = new System.Drawing.Point(0, 49);
            this.panelRSA.Name = "panelRSA";
            this.panelRSA.Size = new System.Drawing.Size(784, 490);
            this.panelRSA.TabIndex = 1;
            this.panelRSA.Visible = false;
            // 
            // btnRsaDecrypt
            // 
            this.btnRsaDecrypt.Location = new System.Drawing.Point(284, 421);
            this.btnRsaDecrypt.Name = "btnRsaDecrypt";
            this.btnRsaDecrypt.Size = new System.Drawing.Size(150, 30);
            this.btnRsaDecrypt.TabIndex = 10;
            this.btnRsaDecrypt.Text = "Giải mã (Decrypt)";
            this.btnRsaDecrypt.UseVisualStyleBackColor = true;
            this.btnRsaDecrypt.Click += new System.EventHandler(this.BtnRsaDecrypt_Click);
            // 
            // btnRsaEncrypt
            // 
            this.btnRsaEncrypt.Location = new System.Drawing.Point(128, 421);
            this.btnRsaEncrypt.Name = "btnRsaEncrypt";
            this.btnRsaEncrypt.Size = new System.Drawing.Size(150, 30);
            this.btnRsaEncrypt.TabIndex = 9;
            this.btnRsaEncrypt.Text = "Mã hoá (Encrypt)";
            this.btnRsaEncrypt.UseVisualStyleBackColor = true;
            this.btnRsaEncrypt.Click += new System.EventHandler(this.BtnRsaEncrypt_Click);
            // 
            // txtRsaCiphertext
            // 
            this.txtRsaCiphertext.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtRsaCiphertext.Location = new System.Drawing.Point(128, 371);
            this.txtRsaCiphertext.Multiline = true;
            this.txtRsaCiphertext.Name = "txtRsaCiphertext";
            this.txtRsaCiphertext.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.txtRsaCiphertext.Size = new System.Drawing.Size(644, 40);
            this.txtRsaCiphertext.TabIndex = 8;
            // 
            // lblRsaCiphertext
            // 
            this.lblRsaCiphertext.AutoSize = true;
            this.lblRsaCiphertext.Location = new System.Drawing.Point(15, 376);
            this.lblRsaCiphertext.Name = "lblRsaCiphertext";
            this.lblRsaCiphertext.Size = new System.Drawing.Size(107, 13);
            this.lblRsaCiphertext.TabIndex = 7;
            this.lblRsaCiphertext.Text = "Ciphertext (Base64):";
            // 
            // txtRsaPlaintext
            // 
            this.txtRsaPlaintext.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtRsaPlaintext.Location = new System.Drawing.Point(128, 321);
            this.txtRsaPlaintext.Multiline = true;
            this.txtRsaPlaintext.Name = "txtRsaPlaintext";
            this.txtRsaPlaintext.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.txtRsaPlaintext.Size = new System.Drawing.Size(644, 40);
            this.txtRsaPlaintext.TabIndex = 6;
            // 
            // lblRsaPlaintext
            // 
            this.lblRsaPlaintext.AutoSize = true;
            this.lblRsaPlaintext.Location = new System.Drawing.Point(15, 326);
            this.lblRsaPlaintext.Name = "lblRsaPlaintext";
            this.lblRsaPlaintext.Size = new System.Drawing.Size(94, 13);
            this.lblRsaPlaintext.TabIndex = 5;
            this.lblRsaPlaintext.Text = "Plaintext (Bản rõ):";
            // 
            // txtRsaPrivateKey
            // 
            this.txtRsaPrivateKey.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtRsaPrivateKey.Location = new System.Drawing.Point(18, 222);
            this.txtRsaPrivateKey.Multiline = true;
            this.txtRsaPrivateKey.Name = "txtRsaPrivateKey";
            this.txtRsaPrivateKey.ReadOnly = true;
            this.txtRsaPrivateKey.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.txtRsaPrivateKey.Size = new System.Drawing.Size(754, 80);
            this.txtRsaPrivateKey.TabIndex = 4;
            // 
            // lblRsaPrivateKey
            // 
            this.lblRsaPrivateKey.AutoSize = true;
            this.lblRsaPrivateKey.Location = new System.Drawing.Point(15, 206);
            this.lblRsaPrivateKey.Name = "lblRsaPrivateKey";
            this.lblRsaPrivateKey.Size = new System.Drawing.Size(126, 13);
            this.lblRsaPrivateKey.TabIndex = 3;
            this.lblRsaPrivateKey.Text = "Private Key (Khóa bí mật):";
            // 
            // txtRsaPublicKey
            // 
            this.txtRsaPublicKey.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtRsaPublicKey.Location = new System.Drawing.Point(18, 112);
            this.txtRsaPublicKey.Multiline = true;
            this.txtRsaPublicKey.Name = "txtRsaPublicKey";
            this.txtRsaPublicKey.ReadOnly = true;
            this.txtRsaPublicKey.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.txtRsaPublicKey.Size = new System.Drawing.Size(754, 80);
            this.txtRsaPublicKey.TabIndex = 2;
            // 
            // lblRsaPublicKey
            // 
            this.lblRsaPublicKey.AutoSize = true;
            this.lblRsaPublicKey.Location = new System.Drawing.Point(15, 96);
            this.lblRsaPublicKey.Name = "lblRsaPublicKey";
            this.lblRsaPublicKey.Size = new System.Drawing.Size(135, 13);
            this.lblRsaPublicKey.TabIndex = 1;
            this.lblRsaPublicKey.Text = "Public Key (Khóa công khai):";
            // 
            // btnRsaGenerateKeys
            // 
            this.btnRsaGenerateKeys.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
            | System.Windows.Forms.AnchorStyles.Right)));
            this.btnRsaGenerateKeys.Location = new System.Drawing.Point(18, 14);
            this.btnRsaGenerateKeys.Name = "btnRsaGenerateKeys";
            this.btnRsaGenerateKeys.Size = new System.Drawing.Size(754, 30);
            this.btnRsaGenerateKeys.TabIndex = 0;
            this.btnRsaGenerateKeys.Text = "Tạo bộ khóa Mới (New Keys)";
            this.btnRsaGenerateKeys.UseVisualStyleBackColor = true;
            this.btnRsaGenerateKeys.Click += new System.EventHandler(this.BtnRsaGenerateKeys_Click);
            // 
            // panelPlayfair
            // 
            this.panelPlayfair.Controls.Add(this.btnPlayfairDecrypt);
            this.panelPlayfair.Controls.Add(this.btnPlayfairEncrypt);
            this.panelPlayfair.Controls.Add(this.txtPlayfairCiphertext);
            this.panelPlayfair.Controls.Add(this.lblPlayfairCiphertext);
            this.panelPlayfair.Controls.Add(this.txtPlayfairPlaintext);
            this.panelPlayfair.Controls.Add(this.lblPlayfairPlaintext);
            this.panelPlayfair.Controls.Add(this.txtPlayfairKey);
            this.panelPlayfair.Controls.Add(this.lblPlayfairKey);
            this.panelPlayfair.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panelPlayfair.Location = new System.Drawing.Point(0, 49);
            this.panelPlayfair.Name = "panelPlayfair";
            this.panelPlayfair.Size = new System.Drawing.Size(784, 490);
            this.panelPlayfair.TabIndex = 0;
            this.panelPlayfair.Visible = false;
            // 
            // btnPlayfairDecrypt
            // 
            this.btnPlayfairDecrypt.Location = new System.Drawing.Point(283, 222);
            this.btnPlayfairDecrypt.Name = "btnPlayfairDecrypt";
            this.btnPlayfairDecrypt.Size = new System.Drawing.Size(150, 30);
            this.btnPlayfairDecrypt.TabIndex = 7;
            this.btnPlayfairDecrypt.Text = "Giải mã (Decrypt)";
            this.btnPlayfairDecrypt.UseVisualStyleBackColor = true;
            this.btnPlayfairDecrypt.Click += new System.EventHandler(this.BtnPlayfairDecrypt_Click);
            // 
            // btnPlayfairEncrypt
            // 
            this.btnPlayfairEncrypt.Location = new System.Drawing.Point(127, 222);
            this.btnPlayfairEncrypt.Name = "btnPlayfairEncrypt";
            this.btnPlayfairEncrypt.Size = new System.Drawing.Size(150, 30);
            this.btnPlayfairEncrypt.TabIndex = 6;
            this.btnPlayfairEncrypt.Text = "Mã hoá (Encrypt)";
            this.btnPlayfairEncrypt.UseVisualStyleBackColor = true;
            this.btnPlayfairEncrypt.Click += new System.EventHandler(this.BtnPlayfairEncrypt_Click);
            // 
            // txtPlayfairCiphertext
            // 
            this.txtPlayfairCiphertext.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtPlayfairCiphertext.Location = new System.Drawing.Point(127, 132);
            this.txtPlayfairCiphertext.Multiline = true;
            this.txtPlayfairCiphertext.Name = "txtPlayfairCiphertext";
            this.txtPlayfairCiphertext.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.txtPlayfairCiphertext.Size = new System.Drawing.Size(645, 80);
            this.txtPlayfairCiphertext.TabIndex = 5;
            // 
            // lblPlayfairCiphertext
            // 
            this.lblPlayfairCiphertext.AutoSize = true;
            this.lblPlayfairCiphertext.Location = new System.Drawing.Point(17, 137);
            this.lblPlayfairCiphertext.Name = "lblPlayfairCiphertext";
            this.lblPlayfairCiphertext.Size = new System.Drawing.Size(102, 13);
            this.lblPlayfairCiphertext.TabIndex = 4;
            this.lblPlayfairCiphertext.Text = "Ciphertext (Bản mã):";
            // 
            // txtPlayfairPlaintext
            // 
            this.txtPlayfairPlaintext.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtPlayfairPlaintext.Location = new System.Drawing.Point(127, 42);
            this.txtPlayfairPlaintext.Multiline = true;
            this.txtPlayfairPlaintext.Name = "txtPlayfairPlaintext";
            this.txtPlayfairPlaintext.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.txtPlayfairPlaintext.Size = new System.Drawing.Size(645, 80);
            this.txtPlayfairPlaintext.TabIndex = 3;
            // 
            // lblPlayfairPlaintext
            // 
            this.lblPlayfairPlaintext.AutoSize = true;
            this.lblPlayfairPlaintext.Location = new System.Drawing.Point(17, 47);
            this.lblPlayfairPlaintext.Name = "lblPlayfairPlaintext";
            this.lblPlayfairPlaintext.Size = new System.Drawing.Size(94, 13);
            this.lblPlayfairPlaintext.TabIndex = 2;
            this.lblPlayfairPlaintext.Text = "Plaintext (Bản rõ):";
            // 
            // txtPlayfairKey
            // 
            this.txtPlayfairKey.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtPlayfairKey.Location = new System.Drawing.Point(127, 12);
            this.txtPlayfairKey.Name = "txtPlayfairKey";
            this.txtPlayfairKey.Size = new System.Drawing.Size(645, 20);
            this.txtPlayfairKey.TabIndex = 1;
            // 
            // lblPlayfairKey
            // 
            this.lblPlayfairKey.AutoSize = true;
            this.lblPlayfairKey.Location = new System.Drawing.Point(17, 17);
            this.lblPlayfairKey.Name = "lblPlayfairKey";
            this.lblPlayfairKey.Size = new System.Drawing.Size(64, 13);
            this.lblPlayfairKey.TabIndex = 0;
            this.lblPlayfairKey.Text = "Key (Khóa):";
            // 
            // mainToolStrip
            // 
            this.mainToolStrip.Location = new System.Drawing.Point(0, 24);
            this.mainToolStrip.Name = "mainToolStrip";
            this.mainToolStrip.Size = new System.Drawing.Size(784, 25);
            this.mainToolStrip.TabIndex = 2;
            this.mainToolStrip.Text = "toolStrip1";
            // 
            // mainStatusStrip
            // 
            this.mainStatusStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mainStatusLabel});
            this.mainStatusStrip.Location = new System.Drawing.Point(0, 539);
            this.mainStatusStrip.Name = "mainStatusStrip";
            this.mainStatusStrip.Size = new System.Drawing.Size(784, 22);
            this.mainStatusStrip.TabIndex = 3;
            this.mainStatusStrip.Text = "statusStrip1";
            // 
            // mainStatusLabel
            // 
            this.mainStatusLabel.Name = "mainStatusLabel";
            this.mainStatusLabel.Size = new System.Drawing.Size(42, 17);
            this.mainStatusLabel.Text = "Ready.";
            // 
            // EncryptionForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(784, 561);
            this.Controls.Add(this.panelPlayfair);
            this.Controls.Add(this.panelRSA);
            this.Controls.Add(this.mainStatusStrip);
            this.Controls.Add(this.mainToolStrip);
            this.Controls.Add(this.mainMenuStrip);
            this.MainMenuStrip = this.mainMenuStrip;
            this.MinimumSize = new System.Drawing.Size(600, 400);
            this.Name = "EncryptionForm";
            this.Text = "Encryption App (Giống CrypTool)";
            this.mainMenuStrip.ResumeLayout(false);
            this.mainMenuStrip.PerformLayout();
            this.panelRSA.ResumeLayout(false);
            this.panelRSA.PerformLayout();
            this.panelPlayfair.ResumeLayout(false);
            this.panelPlayfair.PerformLayout();
            this.mainToolStrip.ResumeLayout(false);
            this.mainToolStrip.PerformLayout();
            this.mainStatusStrip.ResumeLayout(false);
            this.mainStatusStrip.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip mainMenuStrip;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exitToolStripMenuItem;
        private System.Windows.Forms.Panel panelPlayfair;
        private System.Windows.Forms.Button btnPlayfairDecrypt;
        private System.Windows.Forms.Button btnPlayfairEncrypt;
        private System.Windows.Forms.TextBox txtPlayfairCiphertext;
        private System.Windows.Forms.Label lblPlayfairCiphertext;
        private System.Windows.Forms.TextBox txtPlayfairPlaintext;
        private System.Windows.Forms.Label lblPlayfairPlaintext;
        private System.Windows.Forms.TextBox txtPlayfairKey;
        private System.Windows.Forms.Label lblPlayfairKey;
        private System.Windows.Forms.Panel panelRSA;
        private System.Windows.Forms.Button btnRsaDecrypt;
        private System.Windows.Forms.Button btnRsaEncrypt;
        private System.Windows.Forms.TextBox txtRsaCiphertext;
        private System.Windows.Forms.Label lblRsaCiphertext;
        private System.Windows.Forms.TextBox txtRsaPlaintext;
        private System.Windows.Forms.Label lblRsaPlaintext;
        private System.Windows.Forms.TextBox txtRsaPrivateKey;
        private System.Windows.Forms.Label lblRsaPrivateKey;
        private System.Windows.Forms.TextBox txtRsaPublicKey;
        private System.Windows.Forms.Label lblRsaPublicKey;
        private System.Windows.Forms.Button btnRsaGenerateKeys;
        private System.Windows.Forms.StatusStrip mainStatusStrip;
        private System.Windows.Forms.ToolStripStatusLabel mainStatusLabel;
        private System.Windows.Forms.ToolStrip mainToolStrip;
        private System.Windows.Forms.ToolStripMenuItem encryptDecryptToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem symmetricclassicToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem playfairToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem asymmetricToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem rsaToolStripMenuItem;
    }
}