import express from "express";
import { createUser, getUsers, getUserById, updateUserById, deleteUserById } from "../controllers/user.controller.js";
import { validate } from "../middlewares/validate.js";
import { userSchema } from "../validations/user.schema.js";

const router = express.Router();

// Create user
router.post("/", validate(userSchema), createUser);

// Get all users
router.get("/", getUsers);

// Get user by ID
router.get("/:id", getUserById);

// Update user by ID
router.put("/:id", validate(userSchema), updateUserById);

// Delete user by ID
router.delete("/:id", deleteUserById);

export default router;