import Product from "../models/product.model.js";

class ProductRepository {

  async create(data) {
    return Product.create(data);
  }

  async find(filter, options = {}) {
    const { sort = {}, skip = 0, limit = 10 } = options;

    console.log("FILTER:", filter);
    console.log("SKIP:", skip);
    console.log("LIMIT:", limit);

    return Product.find(filter)
      .sort(sort)
      .skip(skip)
      .limit(limit);
  }

  async count(filter) {
    return Product.countDocuments(filter);
  }

  async softDelete(id) {
    return Product.findByIdAndUpdate(
      id,
      { deletedAt: new Date() },
      { new: true }
    );
  }

}

export default new ProductRepository();