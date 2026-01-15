import fs from "fs";
import axios from "axios";
import { ENV } from "../config/env.js";
import { extractText } from "../utils/pdf.util.js";

/* =====================================
   1️⃣ INITIAL ANALYSIS (PDF UPLOAD)
===================================== */
export const analyzeResume = async (req, res) => {
  try {
    const jobDescription = req.body.jobDescription;

    if (!req.file || !jobDescription) {
      return res.status(400).json({
        success: false,
        message: "Resume file or job description missing"
      });
    }

    const resumeText = await extractText(
      req.file.path,
      req.file.mimetype
    );

    const aiResponse = await axios.post(
      `${ENV.AI_URL}/api/resume/analyze`,
      {
        resume_text: resumeText,
        job_description: jobDescription
      },
      { timeout: 60_000 }
    );

    fs.unlink(req.file.path, () => {});

    return res.json({
      success: true,
      data: aiResponse.data
    });

  } catch (err) {
    console.error("❌ ANALYZE ERROR:", err.message);
    return res.status(500).json({
      success: false,
      message: "Resume analysis failed"
    });
  }
};

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
