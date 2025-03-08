const FeaturesSection = () => {
    const features = [
      {
        icon: 'studio-microphone',
        title: 'Book Studios',
        text: 'Find and reserve professional recording studios'
      },
      {
        icon: 'users',
        title: 'Collaborate',
        text: 'Work with musicians worldwide in real-time'
      },
      {
        icon: 'calendar',
        title: 'Manage Events',
        text: 'Organize concerts and rehearsals effortlessly'
      }
    ];
  
    return (
      <section id="features" className="py-20">
        <div className="container mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">Features</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <div key={index} className="text-center p-6 rounded-lg hover:bg-gray-100">
                <div className="text-4xl mb-4">{/* Icon component */}</div>
                <h3 className="text-xl font-bold mb-2">{feature.title}</h3>
                <p>{feature.text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
    );
  };
  
  export default FeaturesSection;