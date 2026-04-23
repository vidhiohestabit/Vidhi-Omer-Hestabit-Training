import productRepository from "../repositories/product.repository.js";
import ApiError from "../utils/ApiError.js";

class ProductService {
  async create(data) {
    return productRepository.create(data);
  }

  async getAll(query) {
    const {
      search,
      minPrice,
      maxPrice,
      sort,
      tags,
      page,
      limit,
      includeDeleted
    } = query;

    let filter = {};
    const includeDeletedFlag = includeDeleted === "true";
    if (!includeDeletedFlag) {
      filter.deletedAt = null;
    }

    if (search) {
      filter.$or = [
        { name: { $regex: search, $options: "i" } },
        { tags: { $regex: search, $options: "i" } }
      ];
    }

    if (minPrice || maxPrice) {
      filter.price = {};
      if (minPrice) filter.price.$gte = Number(minPrice);
      if (maxPrice) filter.price.$lte = Number(maxPrice);
    }

    let sortOption = {};
    if (sort) {
      const [field, order] = sort.split(":");
      sortOption[field] = order === "desc" ? -1 : 1;
    }

    // 👉 If pagination not requested
    if (!page && !limit) {
      return productRepository.find(filter, { sort: sortOption });
    }

    const pageNumber = Number(page) || 1;
    const limitNumber = Number(limit) || 10;

    const skip = (pageNumber - 1) * limitNumber;

    const products = await productRepository.find(filter, {
      sort: sortOption,
      skip,
      limit: limitNumber
    });

    const total = await productRepository.count(filter);

    return {
      total,
      page: pageNumber,
      limit: limitNumber,
      products
    };
  }
}

export default new ProductService();