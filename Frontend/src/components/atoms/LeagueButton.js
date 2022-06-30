import React, {useState, useEffect} from "react";
import {
    Grid,
    Box,
    Button,
} from "@mui/material";

export default function LeagueButton(props){
    return (
        <Button 
            sx={{m:1, p:1, border:1}}
            onClick={()=>{
                props.setLeague(props.league);
            }}
        >
            <Box>
                {props.league.league_name}
            </Box>
            <Box sx={{fontSize:12}}>
                {props.league.team}
            </Box>
        </Button>
    )
}