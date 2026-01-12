import express from "express";
import { matchResumeWithJob } from "../controllers/match.controller.js";

const router = express.Router();

router.post("/", matchResumeWithJob);

export default router;
