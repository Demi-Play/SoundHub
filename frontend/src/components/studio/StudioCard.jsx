const StudioCard = ({ studio }) => {
    return (
      <div className="studio-card">
        <img src={studio.image} alt={studio.name} />
        <div className="details">
          <h3>{studio.name}</h3>
          <p>{studio.address}</p>
          <p>${studio.price_per_hour}/hour</p>
          <button>Book Now</button>
        </div>
      </div>
    );
  };
  
  export default StudioCard;