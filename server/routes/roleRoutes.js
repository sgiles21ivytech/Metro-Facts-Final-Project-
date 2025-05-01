import express from "express";
import { getRoles, createRole } from "../controllers/rolesController.js";

const router = express.Router();

router.get("/", getRoles);
router.post("/", createRole);

export default router;
