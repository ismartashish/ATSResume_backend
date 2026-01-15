import fs from "fs";
import axios from "axios";
import { ENV } from "../config/env.js";
import { extractText } from "../utils/pdf.util.js";



export const analyzeResume = async (req, res) => {
  try {
    const jobDescription = req.body.jobDescription;

    if (!req.file || !jobDescription) {
      return res.status(400).json({ message: "Missing data" });
    }

    const resumeText = await extractText(
      req.file.path,
      req.file.mimetype
    );

    const aiRes = await axios.post(
      "https://atsresume-ai.onrender.com/analyze",
      {
        resume_text: resumeText,
        job_description: jobDescription
      },
      {
        headers: {
          "Content-Type": "application/json"
        }
      }
    );

    res.json({
      success: true,
      data: aiRes.data
    });

  } catch (err) {
    console.error("AI ERROR:", err.response?.data || err.message);
    res.status(500).json({ message: "AI analysis failed" });
  }
};
