import React, {useState, useEffect} from "react";
import {
    Grid,
    Box,
} from "@mui/material";

export default function LeagueButton(props){

    return (
        <Box sx={{m:1, p:1, border:1}}>
            <Box>
                {props.leagueName}
            </Box>
            <Box sx={{fontSize:12}}>
                {props.teamName}
            </Box>
        </Box>
    )
}