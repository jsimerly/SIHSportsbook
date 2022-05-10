import React, { Component } from "react";
import { 
    Grid,
    Box,
    Divider
} from "@mui/material";
import MatchUp from "../molecules/MatchUp";

export default function Matchups(props){
    const matchups = (
        <Box>
            {['Matchup 1', 'Matchup 2', 'Matchup 3', 'Matchup 4', 'Matchup 5'].map((matchup, index) =>
                <MatchUp/>
            )}
        </Box>
   )
   
    return (
        <div>{matchups}</div>
    )
}
  