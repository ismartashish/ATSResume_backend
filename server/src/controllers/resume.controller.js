import fs from "fs";
import axios from "axios";
import { ENV } from "../config/env.js";
import { extractText } from "../utils/pdf.util.js";

/* =====================================
   1️⃣ INITIAL ANALYSIS (PDF UPLOAD)
===================================== */
const aiResponse = await axios.post(
  `${ENV.AI_URL}/api/resume/analyze`,
  {
    resume_text: resumeText,
    job_description: jobDescription
  },
  {
    headers: {
      "Content-Type": "application/json"
    },
    timeout: 60000
  }
);


/* =====================================
   2️⃣ LIVE RE-ANALYSIS (TEXT ONLY)
===================================== */
export const reanalyzeResume = async (req, res) => {
  try {
    const { resume_text, job_description } = req.body;

    if (!resume_text || !job_description) {
      return res.status(400).json({
        success: false,
        message: "Missing resume text or job description"
      });
    }

    const aiResponse = await axios.post(
      `${ENV.AI_URL}/api/resume/analyze`,
      {
        resume_text,
        job_description
      },
      { timeout: 60_000 }
    );

    return res.json({
      success: true,
      data: aiResponse.data
    });

  } catch (err) {
    console.error("❌ REANALYZE ERROR:", err.message);
    return res.status(500).json({
      success: false,
      message: "Live re-analysis failed"
    });
  }
};
