import React, { useState } from "react";
import { Box, Button } from "@mui/material";
import Rows from "./playground2";

export default function PlaygroundMain(props) {
  //This data can come in at different lengths
  const fetchData = [
    {
      info: "info1",
      data: { data1: 11, data2: 12, data3: 13 }
    },
    {
      info: "info2",
      data: { data1: 21, data2: 22, data3: 23 }
    },
    {
      info: "info3",
      data: { data1: 31, data2: 32, data3: 33 }
    }
  ];

  const [selectedButtons, setSelectedButtons] = useState([]);

  function handleButtonSelected(button) {
    const newButtons = selectedButtons;
    if (!newButtons.includes(button)) {
      newButtons.push(button);
    } else {
      newButtons.splice(newButtons.indexOf(button), 1);
    }
    setSelectedButtons([...newButtons]);
  }

  function handle(i) {
    setSelectedButtons([
      ...selectedButtons.slice(0, i),
      ...selectedButtons.slice(i + 1)
    ]);
  }

  return (
    <Box>
      {fetchData.map((row, index) => {
        return (
          <Rows
            dataFromParent={row}
            selectHandler={handleButtonSelected}
            selectedButtons={selectedButtons}
          />
        );
      })}
      {selectedButtons.map((num, index) => {
        return <Button onClick={() => handle(index)}> {num} </Button>;
      })}
    </Box>
  );
}

