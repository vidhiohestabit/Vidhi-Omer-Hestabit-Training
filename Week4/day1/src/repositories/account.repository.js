import Account from "../models/Account.js";

class AccountRepository {
  async create(data) {
    return await Account.create(data);
  }

  async findByEmail(email) {
    return await Account.findOne({ email });
  }
}

export default new AccountRepository();