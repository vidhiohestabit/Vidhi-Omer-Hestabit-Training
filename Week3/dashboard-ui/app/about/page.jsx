import Card from "../../components/ui/Card";
import Badge from "../../components/ui/Badge";

export default function AboutPage() {
  return (
    <div className="space-y-10">

      {/* Hero */}
      <div className="bg-gradient-to-r from-green-400 to-teal-500 rounded-xl p-8 text-white">
        <h1 className="text-3xl font-bold mb-2">About Purity UI</h1>
        <p className="text-sm max-w-2xl opacity-90">
          A modern admin dashboard built with Next.js & TailwindCSS,
          focusing on clean architecture, reusable components,
          and real-world SaaS design patterns.
        </p>
      </div>

      {/* Intro */}
      <Card>
        <h2 className="text-xl font-semibold mb-3">
          What is Purity UI Dashboard?
        </h2>
        <p className="text-gray-600 text-sm leading-relaxed max-w-3xl">
          Purity UI Dashboard is a frontend-only admin panel created
          to demonstrate scalable UI systems using modern web technologies.
          It emphasizes clean layouts, responsive design, and component-driven
          development suitable for real production environments.
        </p>
      </Card>

      {/* Highlights */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        {[
          { label: "Pages", value: "10+" },
          { label: "Reusable Components", value: "15+" },
          { label: "Responsive Layouts", value: "100%" },
          { label: "Backend", value: "None" },
        ].map((item) => (
          <Card key={item.label} className="text-center">
            <h3 className="text-2xl font-bold">{item.value}</h3>
            <p className="text-sm text-gray-500 mt-1">{item.label}</p>
          </Card>
        ))}
      </div>

      {/* Features */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card>
          <Badge>UI</Badge>
          <h3 className="text-lg font-semibold mt-4 mb-2">
            Reusable Components
          </h3>
          <p className="text-sm text-gray-600">
            Atomic UI components like buttons, cards, badges,
            and inputs designed to be reused across pages
            while maintaining visual consistency.
          </p>
        </Card>

        <Card>
          <Badge>UX</Badge>
          <h3 className="text-lg font-semibold mt-4 mb-2">
            Scalable Layout System
          </h3>
          <p className="text-sm text-gray-600">
            Next.js App Router with nested layouts allows
            shared navigation, better separation of concerns,
            and smooth page transitions.
          </p>
        </Card>

        <Card>
          <Badge>Tech</Badge>
          <h3 className="text-lg font-semibold mt-4 mb-2">
            Modern Frontend Stack
          </h3>
          <p className="text-sm text-gray-600">
            Built using Next.js, TailwindCSS, and modern
            frontend best practices to ensure performance,
            flexibility, and maintainability.
          </p>
        </Card>
      </div>

      {/* Why Section */}
      <Card>
        <h2 className="text-xl font-semibold mb-3">
          Why This Project Exists
        </h2>
        <p className="text-sm text-gray-600 leading-relaxed max-w-3xl">
          This project was built as a learning-focused capstone to understand
          how real-world admin dashboards are structured.
          It demonstrates routing, layout composition, component reuse,
          responsive design, and UI consistency — without relying on a backend.
        </p>
      </Card>

      {/* Roadmap */}
      <Card>
        <h2 className="text-xl font-semibold mb-4">
          Roadmap & Future Improvements
        </h2>
        <ul className="space-y-3 text-sm text-gray-600">
          <li>🚀 Backend integration (Auth, API, DB)</li>
          <li>📊 Charts & analytics</li>
          <li>🔒 Role-based access control</li>
          <li>🎨 Theme customization</li>
        </ul>
      </Card>

    </div>
  );
}
