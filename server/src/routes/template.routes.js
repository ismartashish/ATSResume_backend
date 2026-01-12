import express from "express";
import { getTemplates } from "../controllers/template.controller.js";

const router = express.Router();

router.get("/", getTemplates);

export default router;
