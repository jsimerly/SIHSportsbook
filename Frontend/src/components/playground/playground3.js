import React from "react";
import { ToggleButton } from "@mui/material";

export default function ClickableButton(props) {
  function buttonSelected(e) {
    props.selectHandler(props.text);
  }

  console.log(props.selectedButtons);

  return (
    <ToggleButton
      selected={props.selectedButtons.includes(props.text) ? true : false}
      onChange={buttonSelected}
    >
      {props.text}
    </ToggleButton>
  );
}