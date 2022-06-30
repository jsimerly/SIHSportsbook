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
            sx={{mt:.5, p:1, border:1}}
            fullWidth
            onClick={()=>{
                
                props.setLeague(props.league);
                navigate('/sportsbook/' + props.league.league_id)
            }}
        >
            <Box>
                <Box sx={{fontSize:16, align:'left'}}>
                    {props.league.league_name}
                </Box>
                <Box sx={{fontSize:10}}>
                    {props.league.team}
                </Box>
            </Box>
        </Button>
    )
}