import React, {useState, useEffect} from "react";
import {
    Grid,
    Box,
} from "@mui/material";

export default function LeagueButton(props){
    return (
        <Box 
            sx={{m:1, p:1, border:1}}
            onClick={()=>{
                props.setLeague(props.league);
                console.log("CLICK")
            }}
        >
            <Box>
                {props.league.league_name}
            </Box>
            <Box sx={{fontSize:12}}>
                {props.league.team}
            </Box>
        </Box>
    )
}