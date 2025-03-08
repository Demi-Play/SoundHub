const Footer = () => {
    return (
      <footer className="bg-gray-800 py-8 mt-20">
        <div className="container mx-auto text-white text-center">
          <p>&copy; 2025 SoundHub. All rights reserved.</p>
          <div className="mt-4 space-x-4">
            <a href="/terms" className="hover:text-blue-500">Terms</a>
            <a href="/privacy" className="hover:text-blue-500">Privacy</a>
            <a href="/contact" className="hover:text-blue-500">Contact</a>
          </div>
        </div>
      </footer>
    );
  };
  
  export default Footer;