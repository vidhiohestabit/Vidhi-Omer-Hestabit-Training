import Image from "next/image";
import Card from "../components/ui/Card";

export const metadata = {
  title: "Purity UI Dashboard – Modern SaaS Admin",
  description:
    "A modern SaaS dashboard built with Next.js and TailwindCSS. Clean UI, reusable components, and scalable architecture.",
};

export default function HomePage() {
  return (
    <main className="space-y-24">

      {/* ================= HERO SECTION ================= */}
      <section className="flex flex-col-reverse lg:flex-row items-center gap-12">
        <div className="flex-1 space-y-6">
          <h1 className="text-4xl lg:text-5xl font-bold leading-tight">
            Build modern dashboards <br />
            faster with Purity UI
          </h1>

          <p className="text-gray-600 max-w-xl">
            Purity UI Dashboard is a clean and modern SaaS admin template
            built with Next.js App Router and TailwindCSS.
          </p>

          <div className="flex gap-4">
            <a
              href="/dashboard"
              className="px-6 py-3 bg-teal-500 text-white rounded-lg font-medium hover:bg-teal-600"
            >
              View Dashboard
            </a>
            <a
              href="/about"
              className="px-6 py-3 border rounded-lg font-medium hover:bg-gray-100"
            >
              Learn More
            </a>
          </div>
        </div>

        <div className="flex-1">
          <Image
            src="/dashboard-preview.png"
            alt="Dashboard preview"
            width={600}
            height={400}
            className="rounded-xl shadow-lg"
            priority
          />
        </div>
      </section>

      {/* ================= FEATURES ================= */}
      <section>
        <h2 className="text-3xl font-semibold text-center mb-12">
          Everything you need to build fast
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <Card>
            <h3 className="text-lg font-semibold mb-2">Reusable UI</h3>
            <p className="text-sm text-gray-600">
              Built with reusable components following atomic design principles.
            </p>
          </Card>

          <Card>
            <h3 className="text-lg font-semibold mb-2">Next.js App Router</h3>
            <p className="text-sm text-gray-600">
              Scalable routing, nested layouts, and server components.
            </p>
          </Card>

          <Card>
            <h3 className="text-lg font-semibold mb-2">TailwindCSS</h3>
            <p className="text-sm text-gray-600">
              Utility-first styling with responsive and modern layouts.
            </p>
          </Card>
        </div>
      </section>

      {/* ================= TESTIMONIALS ================= */}
      <section>
        <h2 className="text-3xl font-semibold text-center mb-12">
          Loved by developers
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <Card>
            <p className="text-sm text-gray-600 mb-4">
              “This dashboard helped me understand real SaaS architecture.”
            </p>
            <p className="font-semibold">Frontend Intern</p>
          </Card>

          <Card>
            <p className="text-sm text-gray-600 mb-4">
              “Clean layout, great spacing, and perfect for learning Next.js.”
            </p>
            <p className="font-semibold">React Developer</p>
          </Card>

          <Card>
            <p className="text-sm text-gray-600 mb-4">
              “Exactly how production dashboards are structured.”
            </p>
            <p className="font-semibold">UI Engineer</p>
          </Card>
        </div>
      </section>

      {/* ================= FOOTER ================= */}
      <footer className="border-t pt-8 text-center text-sm text-gray-500">
        © {new Date().getFullYear()} Purity UI Dashboard. All rights reserved.
      </footer>

    </main>
  );
}
