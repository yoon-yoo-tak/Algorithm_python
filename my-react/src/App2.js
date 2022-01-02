import { useEffect, useState } from "react";

function App() {
    const [loading, setLoading] = useState(true);
    const [coins, setCoins] = useState([]);
    const [dollor,  setDollor] = useState("");
    const onCahnge = (event) => setDollor(event.target.value);
    
    useEffect(() => {
        fetch("https://api.coinpaprika.com/v1/tickers")
        .then(response =>response.json())
        .then(json => {
            setCoins(json);
            setLoading(false);
        });
    },[])
  return (
    <div>
        <h1>Input your Money! {loading ? "" : `(${coins.length})`}</h1>
        <div>$<input value={dollor} onChange={onCahnge} type = "number" placeholder="Your money?"></input></div>
        {loading ? <strong>Loading...</strong> : 
        <select>
            {coins.map((coin) => 
            <option>
                you can buy {coin.name} ({coin.symbol}) : {dollor / coin.quotes.USD.price} 
            </option>)}
        </select>}
        
    </div>
  );
}

export default App;
