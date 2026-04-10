export default function Modal({ title, children }) {
  return (
    <div className="fixed inset-0 bg-black/40 flex items-center justify-center">
      <div className="bg-white rounded-xl p-6 w-96">
        <h2 className="font-semibold mb-4">{title}</h2>
        {children}
      </div>
    </div>
  );
}
