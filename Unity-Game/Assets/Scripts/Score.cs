using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Score : MonoBehaviour
{
    public Text score;

    public void Start()
    {
        InvokeRepeating("Scoring", 0.0f, 1f); //Repeat this from after 0.0f seconds, every 1f second.
    }

    void Scoring()
    {
        score.text = (Mathf.FloorToInt(-GameObject.Find("player").transform.position.x)).ToString("D6");
        //Change the contents of the score in the corner to a 6 digit string of the integer floor of the float of the player's X location.
        //TL;DR- A "close enough" integer value of how far to the left you've been going
    }
}