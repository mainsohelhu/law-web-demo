require('dotenv').config();
const express = require('express');
const nodemailer = require('nodemailer');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// ── Middleware ────────────────────────────────────────────────────────────────
app.use(cors());
app.use(express.json());
app.use(express.static('.'));   // serves index.html + assets from project root

// ── Nodemailer transporter ────────────────────────────────────────────────────
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL_USER,        // your Gmail address
    pass: process.env.EMAIL_PASS         // Gmail App Password (not your login password)
  }
});

// ── POST /api/contact ─────────────────────────────────────────────────────────
app.post('/api/contact', async (req, res) => {
  const { name, email, phone, message } = req.body;

  // Basic validation
  if (!name || !email || !message) {
    return res.status(400).json({ success: false, error: 'Name, email, and message are required.' });
  }

  // Email sent TO the firm
  const firmMail = {
    from: `"Insiya Lex Website" <${process.env.EMAIL_USER}>`,
    to: process.env.RECIPIENT_EMAIL || process.env.EMAIL_USER,
    replyTo: email,
    subject: `New Inquiry from ${name}`,
    html: `
      <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e0e0e0; border-radius: 8px;">
        <h2 style="color: #1e3c72; border-bottom: 2px solid #d4af37; padding-bottom: 10px;">New Contact Form Submission</h2>
        <table style="width: 100%; border-collapse: collapse;">
          <tr style="background: #f9f9f9;">
            <td style="padding: 10px; font-weight: bold; width: 130px;">Name</td>
            <td style="padding: 10px;">${name}</td>
          </tr>
          <tr>
            <td style="padding: 10px; font-weight: bold;">Email</td>
            <td style="padding: 10px;"><a href="mailto:${email}">${email}</a></td>
          </tr>
          <tr style="background: #f9f9f9;">
            <td style="padding: 10px; font-weight: bold;">Phone</td>
            <td style="padding: 10px;">${phone || 'Not provided'}</td>
          </tr>
          <tr>
            <td style="padding: 10px; font-weight: bold; vertical-align: top;">Message</td>
            <td style="padding: 10px; white-space: pre-wrap;">${message}</td>
          </tr>
        </table>
        <p style="margin-top: 20px; color: #888; font-size: 12px;">Sent from insiyalex.com contact form</p>
      </div>
    `
  };

  // Auto-reply TO the sender
  const autoReply = {
    from: `"Insiya Lex LLP" <${process.env.EMAIL_USER}>`,
    to: email,
    subject: 'We received your message — Insiya Lex LLP',
    html: `
      <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e0e0e0; border-radius: 8px;">
        <h2 style="color: #1e3c72;">Thanks for reaching out, ${name}.</h2>
        <p style="color: #444; line-height: 1.6;">
          We've received your message and will get back to you within one business day.
          If your matter is urgent, reply directly to this email or WhatsApp us.
        </p>
        <hr style="border: none; border-top: 1px solid #e0e0e0; margin: 20px 0;">
        <p style="color: #888; font-size: 13px;">
          <strong>Insiya Lex LLP</strong><br>
          Remote Paralegal Support for U.S. Law Firms<br>
          <a href="mailto:contact@insiyalex.com" style="color: #d4af37;">contact@insiyalex.com</a>
        </p>
      </div>
    `
  };

  try {
    await transporter.sendMail(firmMail);
    await transporter.sendMail(autoReply);
    res.json({ success: true, message: 'Email sent successfully.' });
  } catch (err) {
    console.error('Email error:', err.message);
    res.status(500).json({ success: false, error: 'Failed to send email. Please try again.' });
  }
});

// ── Start server ──────────────────────────────────────────────────────────────
app.listen(PORT, () => {
  console.log(`Insiya Lex server running on http://localhost:${PORT}`);
});
