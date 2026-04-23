import Card from "@/components/ui/Card";
import Button from "@/components/ui/Button";
import Badge from "@/components/ui/Badge";

export default function BillingPage() {
  return (
    <div className="space-y-10">

      {/* Header */}
      <div>
        <h1 className="text-2xl font-semibold">Billing</h1>
        <p className="text-sm text-gray-500">
          Manage your subscription, payment methods, and invoices
        </p>
      </div>

      {/* Current Plan */}
      <Card>
        <div className="flex flex-col md:flex-row justify-between gap-6">
          <div>
            <h3 className="text-lg font-semibold mb-1">Current Plan</h3>
            <p className="text-sm text-gray-500 mb-4">
              You are currently subscribed to the Pro plan
            </p>

            <div className="flex items-center gap-3">
              <h2 className="text-3xl font-bold">$29</h2>
              <span className="text-sm text-gray-500">/ month</span>
              <Badge>PRO</Badge>
            </div>

            <ul className="mt-4 space-y-2 text-sm text-gray-600">
              <li>✔ Unlimited users</li>
              <li>✔ Advanced analytics</li>
              <li>✔ Priority support</li>
            </ul>
          </div>

          <div className="flex items-center">
            <Button>Upgrade Plan</Button>
          </div>
        </div>
      </Card>

      {/* Payment Method */}
      <Card>
        <h3 className="text-lg font-semibold mb-4">Payment Method</h3>

        <div className="flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="w-12 h-8 bg-gray-200 rounded flex items-center justify-center text-xs font-semibold">
              VISA
            </div>
            <div>
              <p className="text-sm font-medium">Visa ending in 4242</p>
              <p className="text-xs text-gray-500">
                Expiry 08/2027
              </p>
            </div>
          </div>

          <Button variant="secondary">Update</Button>
        </div>
      </Card>

      {/* Billing History */}
      <Card>
        <h3 className="text-lg font-semibold mb-4">Billing History</h3>

        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead className="bg-gray-50 text-gray-500">
              <tr>
                <th className="px-4 py-3 text-left">Invoice</th>
                <th className="px-4 py-3 text-left">Date</th>
                <th className="px-4 py-3 text-left">Amount</th>
                <th className="px-4 py-3 text-left">Status</th>
              </tr>
            </thead>

            <tbody>
              {[
                { id: "#INV-001", date: "Jan 15, 2025", amount: "$29.00", status: "Paid" },
                { id: "#INV-002", date: "Feb 15, 2025", amount: "$29.00", status: "Paid" },
                { id: "#INV-003", date: "Mar 15, 2025", amount: "$29.00", status: "Pending" },
              ].map((invoice) => (
                <tr key={invoice.id} className="border-t">
                  <td className="px-4 py-3">{invoice.id}</td>
                  <td className="px-4 py-3">{invoice.date}</td>
                  <td className="px-4 py-3">{invoice.amount}</td>
                  <td className="px-4 py-3">
                    <span
                      className={`px-3 py-1 rounded-full text-xs font-medium ${
                        invoice.status === "Paid"
                          ? "bg-green-100 text-green-600"
                          : "bg-yellow-100 text-yellow-600"
                      }`}
                    >
                      {invoice.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Card>

      {/* Usage */}
      <Card>
        <h3 className="text-lg font-semibold mb-4">Usage Overview</h3>

        <div className="space-y-4">
          <div>
            <div className="flex justify-between text-sm mb-1">
              <span>API Requests</span>
              <span>7,500 / 10,000</span>
            </div>
            <div className="h-2 bg-gray-200 rounded">
              <div className="h-2 w-3/4 bg-teal-500 rounded" />
            </div>
          </div>

          <div>
            <div className="flex justify-between text-sm mb-1">
              <span>Storage</span>
              <span>12GB / 20GB</span>
            </div>
            <div className="h-2 bg-gray-200 rounded">
              <div className="h-2 w-3/5 bg-indigo-500 rounded" />
            </div>
          </div>
        </div>
      </Card>

    </div>
  );
}
