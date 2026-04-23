import Order from "../models/Order.js";

class OrderRepository {
  async create(data) {
    return await Order.create(data);
  }

  async findById(id) {
    return await Order.findById(id).populate("accountId");
  }

  async findPaginated({ page = 1, limit = 10, status }) {
    const skip = (page - 1) * limit;

    const filter = status ? { status } : {};

    const data = await Order.find(filter)
      .sort({ createdAt: -1 })
      .skip(skip)
      .limit(limit)
      .populate("accountId");

    const total = await Order.countDocuments(filter);

    return {
      total,
      page,
      limit,
      data,
    };
  }

  async update(id, data) {
    return await Order.findByIdAndUpdate(id, data, { new: true });
  }

  async delete(id) {
    return await Order.findByIdAndDelete(id);
  }
}

export default new OrderRepository();