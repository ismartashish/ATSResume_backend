import express from "express";
import multer from "multer";
import {
  analyzeResume,
  reanalyzeResume
} from "../controllers/resume.controller.js";

const router = express.Router();

/* File upload config */
const upload = multer({
  dest: "uploads/resumes",
  limits: { fileSize: 5 * 1024 * 1024 }, // 5MB
});

/* INITIAL ANALYSIS (PDF upload) */
router.post(
  "/analyze",
  upload.single("resume"),
  analyzeResume
);

/* LIVE RE-ANALYSIS (Editor text) */
router.post(
  "/reanalyze",
  reanalyzeResume
);

export default router;
