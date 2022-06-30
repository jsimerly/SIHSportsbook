import React, {useState, useEffect} from "react";
import {
    Grid,
    Box,
    Button,
} from "@mui/material";
import {useNavigate} from 'react-router-dom';

export default function LeagueButton(props){
    let navigate = useNavigate()

    return (
        <Button 
            sx={{m:1, p:1, border:1}}
            onClick={()=>{
                
                props.setLeague(props.league);
                navigate('/sportsbook/' + props.league.league_id)
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