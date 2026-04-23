import Card from "../../components/ui/Card";
import Badge from "../../components/ui/Badge";

export default function DashboardPage() {
  return (
    <div className="space-y-8">

      {/* Top Stats */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
        {[
          { title: "Today's Money", value: "﹩$53,000", badge: "+55%", icon: "💰" },
          { title: "Today's Users", value: "2,300", badge: "+5%", icon: "👥" },
          { title: "New Clients", value: "3,052", badge: "-14%", icon: "🧑‍💼" },
          { title: "Total Sales", value: "$173,000", badge: "+8%", icon: "📈" },
        ].map((item) => (
          <Card key={item.title}>
            <div className="flex items-center justify-between">
              <p className="text-sm text-gray-500">{item.title}</p>
              <span className="text-xl">{item.icon}</span>
            </div>
            <div className="flex items-center justify-between mt-3">
              <h3 className="text-2xl font-semibold">{item.value}</h3>
              <Badge>{item.badge}</Badge>
            </div>
          </Card>
        ))}
      </div>

      {/* Middle Section */}
      <div className="grid grid-cols-1 gap-6">

        {/* Welcome Card */}
        <div className="xl:col-span-2">
          <Card>
            <p className="text-sm text-gray-500 mb-2">Built by developers</p>
            <h2 className="text-xl font-semibold mb-2">
              Purity UI Dashboard
            </h2>
            <p className="text-gray-600 text-sm mb-4 max-w-xl">
              From colors, cards, typography to complex elements,
              you will find the full documentation and reusable components.
            </p>

            <div className="flex items-center gap-4">
              <button className="px-4 py-2 bg-teal-500 text-white text-sm rounded-lg">
                Get Started
              </button>
              <button className="text-teal-500 text-sm font-medium">
                Read Docs →
              </button>
            </div>
          </Card>
        </div>

        {/* Performance */}
        <Card>
          <h3 className="text-lg font-semibold mb-3">
            Weekly Performance
          </h3>
          <p className="text-sm text-gray-500 mb-4">
            Sales performance this week
          </p>

          <div className="space-y-3">
            <div>
              <div className="flex justify-between text-sm mb-1">
                <span>Sales</span>
                <span>75%</span>
              </div>
              <div className="h-2 bg-gray-200 rounded">
                <div className="h-2 w-3/4 bg-teal-500 rounded" />
              </div>
            </div>

            <div>
              <div className="flex justify-between text-sm mb-1">
                <span>Users</span>
                <span>60%</span>
              </div>
              <div className="h-2 bg-gray-200 rounded">
                <div className="h-2 w-3/5 bg-indigo-500 rounded" />
              </div>
            </div>
          </div>
        </Card>
      </div>

      {/* Bottom Section */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

        {/* Recent Activity */}
        <Card>
          <h3 className="text-lg font-semibold mb-4">Recent Activity</h3>
          <ul className="space-y-3 text-sm text-gray-600">
            <li>✅ New user registered</li>
            <li>📦 Order #4567 completed</li>
            <li>💬 Support ticket resolved</li>
            <li>📊 Weekly report generated</li>
          </ul>
        </Card>

        {/* Quick Actions */}
        <Card>
          <h3 className="text-lg font-semibold mb-4">Quick Actions</h3>
          <div className="grid grid-cols-2 gap-4">
            <button className="border rounded-lg py-3 text-sm hover:bg-gray-50 onclick: function() { alert('Add User clicked');!}">
              ➕ Add User
            </button>
            <button className="border rounded-lg py-3 text-sm hover:bg-gray-50">
              📄 View Reports
            </button>
            <button className="border rounded-lg py-3 text-sm hover:bg-gray-50">
              ⚙️ Settings
            </button>
            <button className="border rounded-lg py-3 text-sm hover:bg-gray-50">
              📬 Messages
            </button>
          </div>
        </Card>
      </div>

    </div>
  );
}
