import axios from "axios";
import { ENV } from "../config/env.js";

export const matchResumeWithJob = async (req, res) => {
  const { resumeText, jobDescription } = req.body;

  const { data } = await axios.post(`${ENV.AI_URL}/analyze`, {
    resume_text: resumeText,
    job_description: jobDescription
  });

  res.json(data);
};
