import express from "express";
import {
  getReports,
  createReport,
  getReportById,
} from "../controllers/reportsController.js";
import { verifyToken } from "../middleware/authMiddleware.js";

const router = express.Router();

router.get("/", verifyToken, getReports);
router.post("/", verifyToken, createReport);
router.get("/:id", verifyToken, getReportById);

export default router;
