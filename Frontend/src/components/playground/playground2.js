import React, { useState } from "react";
import { Grid } from "@mui/material";

import ClickableButton from "./playground3";

export default function Rows(props) {
  function handleButtonSelected(button) {
    props.selectHandler(button);
  }

  return (
    <Grid container>
      <Grid item>
        <ClickableButton
          text={props.dataFromParent.data.data1}
          selectHandler={handleButtonSelected}
          selectedButtons={props.selectedButtons}
        />
      </Grid>
      <Grid item>
        <ClickableButton
          text={props.dataFromParent.data.data2}
          selectHandler={handleButtonSelected}
          selectedButtons={props.selectedButtons}
        />
      </Grid>
      <Grid item>
        <ClickableButton
          text={props.dataFromParent.data.data3}
          selectHandler={handleButtonSelected}
          selectedButtons={props.selectedButtons}
        />
      </Grid>
    </Grid>
  );
}
