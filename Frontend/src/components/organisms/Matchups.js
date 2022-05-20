import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    Divider,
    ToggleButtonGroup
} from "@mui/material";
import MatchUp from "../molecules/MatchUp";

export default function Matchups(props){
    const matchupsJson = props.data

    const matchupsDiv = (  
        <Box> 
            <ToggleButtonGroup
                onChange = {props.handleBetSelected}
                fullWidth="true"
                orientation="vertical"
            >            
            {matchupsJson.map((matchupJson, index) => {
                const matchupData = matchupJson
                return (
                   <MatchUp 
                        matchupData={matchupData}
                        betSelectedHandler={props.betSelectedHandler}
                        selectedBets={props.selectedBets}
                        checkDupsIndex={props.checkDupsIndex}
                    />
                )
            })}
            </ToggleButtonGroup>
        </Box>
   )
   
    return (
        <div>{matchupsDiv}</div>
    )
}
  