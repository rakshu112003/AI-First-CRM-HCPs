import { useState } from "react";
import axios from "axios";

const API = "http://127.0.0.1:8000";

function App() {

  const [hcp, setHcp] = useState({
    name: "",
    specialization: "",
    hospital: "",
    city: ""
  });

  const [interaction, setInteraction] = useState({
    hcp_id: 1,
    notes: ""
  });

  const [result, setResult] = useState("");

  const addHCP = async () => {
    console.log("Add HCP clicked", hcp);

    try {
      const response = await axios.post(
        `${API}/hcps/`,
        hcp
      );

      console.log(response.data);
      alert("HCP Added Successfully ✅");

    } catch (error) {
      console.log(error);
      alert("HCP Add Failed ❌ Check backend");
    }
  };


  const addInteraction = async () => {
    console.log("Interaction clicked", interaction);

    try {
      const response = await axios.post(
        `${API}/interactions/`,
        interaction
      );

      console.log(response.data);

      setResult(
        JSON.stringify(response.data, null, 2)
      );

    } catch (error) {
      console.log(error);
      alert("AI Analysis Failed ❌");
    }
  };


  return (
    <div style={{
      padding:"30px",
      fontFamily:"Arial"
    }}>

      <h1>AI-First CRM for HCPs</h1>


      <h2>Add HCP</h2>

      <input
        placeholder="Name"
        value={hcp.name}
        onChange={(e)=>
          setHcp({...hcp,name:e.target.value})
        }
      />

      <br/>

      <input
        placeholder="Specialization"
        value={hcp.specialization}
        onChange={(e)=>
          setHcp({...hcp,specialization:e.target.value})
        }
      />

      <br/>

      <input
        placeholder="Hospital"
        value={hcp.hospital}
        onChange={(e)=>
          setHcp({...hcp,hospital:e.target.value})
        }
      />

      <br/>

      <input
        placeholder="City"
        value={hcp.city}
        onChange={(e)=>
          setHcp({...hcp,city:e.target.value})
        }
      />

      <br/><br/>

      <button onClick={addHCP}>
        Add HCP
      </button>


      <hr/>


      <h2>Add Interaction</h2>

      <input
        placeholder="HCP ID"
        type="number"
        value={interaction.hcp_id}
        onChange={(e)=>
          setInteraction({
            ...interaction,
            hcp_id:Number(e.target.value)
          })
        }
      />

      <br/>

      <textarea
        placeholder="Doctor interaction notes"
        value={interaction.notes}
        onChange={(e)=>
          setInteraction({
            ...interaction,
            notes:e.target.value
          })
        }
      />

      <br/><br/>

      <button onClick={addInteraction}>
        Analyze Interaction
      </button>


      <h2>AI Result</h2>

      <pre>
        {result}
      </pre>


    </div>
  );
}

export default App;
