

const HeroSection = () => {
    return (
        <section className="bg-gradient-to-r from-blue-600 to-purple-600 py-20">
            <div className="container mx-auto text-center text-white">
                <h1 className="text-5xl font-bold mb-4">Create. Collaborate. Record.</h1>
                <p className="text-xl mb-8">The ultimate platform for musicians and studios</p>
                <button
                    className="bg-white text-blue-600 px-8 py-4 rounded-full font-bold hover:bg-blue-100"
                    onClick={() => document.getElementById('features').scrollIntoView()}
                >
                    Learn More
                </button>
            </div>
        </section>
    );
};

export default HeroSection;