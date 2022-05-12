import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    Divider,
    ToggleButtonGroup
} from "@mui/material";
import MatchUp from "../molecules/MatchUp";

export default function Matchups(props){
    const matchupsJson = [
        {
        id: 1,
        data: { 
            team1: "Team 1",
            team2: "Team 2",
            over: "220",
            under: "220",
            sp_pos: "+3.5",
            sp_neg: "-3.5",
            ml_pos: +210,
            ml_neg: -180
        }},
        {
        id: 2,    
        data: { 
            team1: "Team 3",
            team2: "Team 4",
            over: "120",
            under: "120",
            sp_pos: "+5.5",
            sp_neg: "-5.5",
            ml_pos: 115,
            ml_neg: -129,
        }},
        {
        id: 3,    
        data: { 
            team1: "Team 5",
            team2: "Team 6",
            over: "120",
            under: "120",
            sp_pos: "+5.5",
            sp_neg: "-5.5",
            ml_pos: 115,
            ml_neg: -129
        }},
    ]

    const [matchups, setMatchups] = useState(matchupsJson);

    const matchupsDiv = (
        <Box>
            <ToggleButtonGroup 
                fullWidth="true"
                orientation="vertical"
            >            
            {matchups.map((matchupJson, index) => {
                const matchupData = matchupJson
                console.log(matchupData)
                return (
                   <MatchUp data={matchupData}/>
                )
            })}
            </ToggleButtonGroup>
        </Box>
   )
   
    return (
        <div>{matchupsDiv}</div>
    )
}
  