import express from "express";
import {
  createProduct,
  getProducts,
  getProductById,
  updateProductById,
  deleteProductById
} from "../controllers/product.controller.js";
import { validate } from "../middlewares/validate.js";
import { productSchema } from "../validations/product.schema.js";

const router = express.Router();

// Get all products
router.get("/", getProducts);

// Get single product by ID
router.get("/:id", getProductById);

// Create a new product
router.post("/", validate(productSchema), createProduct);

// Update product by ID
router.put("/:id", validate(productSchema), updateProductById);

// Delete product by ID
router.delete("/:id", deleteProductById);

export default router;