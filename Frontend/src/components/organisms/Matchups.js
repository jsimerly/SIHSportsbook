import React, { Component } from "react";
import { 
    Grid,
    Box,
} from "@mui/material";

export default function Matchups(props){
    const matchups = (
        <div>
            <Grid container direction={'column'}>
                {['Matchup 1', 'Matchup 2', 'Matchup 3', 'Matchup 4', 'Matchup 5'].map((matchup, index) =>
                    <Grid container item sx={{border:1}}>
                        {matchup}
                    </Grid>
                )}
            </Grid>
        </div>
    )
        
    return (
    <Box>
        {matchups}
    </Box>
    )
}
  