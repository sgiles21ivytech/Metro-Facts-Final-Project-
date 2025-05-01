import express from "express";
import {
  getMetrics,
  createOrUpdateMetric,
} from "../controllers/metricsController.js";
import { verifyToken } from "../middleware/authMiddleware.js";

const router = express.Router();

router.get("/", verifyToken, getMetrics);
router.post("/", verifyToken, createOrUpdateMetric);

export default router;
