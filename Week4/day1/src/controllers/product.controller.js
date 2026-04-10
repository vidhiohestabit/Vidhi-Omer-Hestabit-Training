import Product from "../models/product.model.js";

import productService from "../services/product.service.js";

export async function getProducts(req, res) {
  try {
    const result = await productService.getAll(req.query);
    res.json(result);
  } catch (err) {
    res.status(500).json({ success: false, message: err.message });
  }
}

// Get product by ID
export async function getProductById(req, res) {
  try {
    const product = await Product.findById(req.params.id);
    if (!product) {
      return res.status(404).json({ success: false, message: "Product not found" });
    }
    res.json(product);
  } catch (err) {
    res.status(500).json({ success: false, message: err.message });
  }
}

// Create a product
export async function createProduct(req, res) {
  try {
    const newProduct = await Product.create(req.body);
    res.status(201).json(newProduct);
  } catch (err) {
    res.status(500).json({ success: false, message: err.message });
  }
}

// Update product by ID
export async function updateProductById(req, res) {
  try {
    const updatedProduct = await Product.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true, runValidators: true }
    );
    if (!updatedProduct) {
      return res.status(404).json({ success: false, message: "Product not found" });
    }
    res.json(updatedProduct);
  } catch (err) {
    res.status(500).json({ success: false, message: err.message });
  }
}

// Delete product by ID
export async function deleteProductById(req, res) {
  try {

    const deletedProduct = await Product.findByIdAndUpdate(
      req.params.id,
      { deletedAt: new Date() },   // mark as deleted
      { new: true }
    );

    if (!deletedProduct) {
      return res.status(404).json({
        success: false,
        message: "Product not found"
      });
    }

    res.json({
      success: true,
      message: "Product soft deleted successfully"
    });

  } catch (err) {
    res.status(500).json({
      success: false,
      message: err.message
    });
  }
}