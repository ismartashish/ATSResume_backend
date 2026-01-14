import fs from "fs";
import axios from "axios";
import { ENV } from "../config/env.js";
import { extractText } from "../utils/pdf.util.js";



export const reanalyzeResume = async (req, res) => {
  try {
    const { resume_text, job_description } = req.body;

    if (!resume_text || !job_description) {
      return res.status(400).json({
        success: false,
        message: "Missing resume text or job description"
      });
    }

    const aiRes = await axios.post("https://atsresume-ai.onrender.com/analyze", {
      resume_text,
      job_description
    });

    res.json({
      success: true,
      ...aiRes.data
    });

  } catch (err) {
    console.error("Reanalyze error:", err.message);
    res.status(500).json({
      success: false,
      message: "Live analysis failed"
    });
  }
};

export const analyzeResume = async (req, res) => {
  try {
    const jobDescription = req.body.jobDescription;

    const resumeText = await extractText(
      req.file.path,
      req.file.mimetype
    );

    const { data } = await axios.post(`${ENV.AI_URL}/analyze`, {
      resume_text: resumeText,
      job_description: jobDescription
    });

    fs.unlinkSync(req.file.path);

    res.json({
      success: true,
      data
    });
  } catch (error) {
    console.error("❌ Resume analysis error:", error);
    res.status(500).json({
      success: false,
      message: "Resume analysis failed"
    });
  }
};
