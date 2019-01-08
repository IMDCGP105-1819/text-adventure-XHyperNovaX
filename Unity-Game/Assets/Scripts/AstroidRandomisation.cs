using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Random = UnityEngine.Random;

public class AstroidRandomisation : MonoBehaviour
{
    private int astroidMovement = 0; //Integer to store the randomised movement 
    private float angle; //Float used to hold the angle the astroid will be facing, in degrees
    private float movementSpeed = 10f; //Base movement speed of 10f
    public bool angularCurve = false; //One of the possible movement choices
    public bool randomMovement = false; //^
    public float spin = 0f; //Curving mid air
    public float playerPositionX; //Hold the player's current position, for localised spawning and despawning
    public float playerPositionY; //^
    public float positionX = 0f; //Astroid's current position
    public float positionY = 0f; //^
    public int randomSelector = 0; //Another random selector
    private Rigidbody2D Arigidbody;
    private CircleCollider2D Acollider; //Renamed for easier use
    private Renderer Arenderer; //Arenderer, Arigidbody, and Acollider for Astroidrenderer etc.

    void Start()
    {
        Arigidbody = GetComponent<Rigidbody2D>();
        Acollider = GetComponent<CircleCollider2D>(); //Get the components
        Arenderer = GetComponent<Renderer>();

        astroidMovement = Random.Range(1, 4); //Random number from 1 to 4
        spin = 0f; //Reset spin
        angle = Random.Range(0f, 360f); //Randomise the angle, in degrees
        playerPositionX = GameObject.Find("player").transform.position.x; //Find the GameObject with the name "player", and save it's X position to playerPositionX
        playerPositionY = GameObject.Find("player").transform.position.y; //^... ...Y position... ...playerPositionY
        randomSelector = Random.Range(1, 2); //Random number, 1 or 2
        if (randomSelector == 1) //If it's 1
            positionX = Random.Range(-4.5f, -2.5f); //the astroid will come further to the left
        else positionX = Random.Range(2.5f, 4.5f); //otherwise, further to the right
        randomSelector = Random.Range(1, 2); //same with up and down
        if (randomSelector == 1)
            positionY = Random.Range(-4.5f, -2.5f);
        else positionY = Random.Range(2.5f, 4.5f);

        Arigidbody.MovePosition(new Vector2(playerPositionX + positionX, playerPositionY + positionY)); //Set the position of the astroid to near you, but with an offset (so they don't spawn on you)
        Arigidbody.MoveRotation(angle); //Set the angle to something random, as saved above in the variable "angle" (still, in degrees)
        switch (astroidMovement) //If the random digit is
        {
            case 1: //1; it will be a normal astroid
                movementSpeed = 10f;
                break;
            case 2: //2; it will have a randomised speed
                movementSpeed = Random.Range(1f, 5f)*10f;
                break;
            case 3: //3; It will have a curve, at normal speed
                angularCurve = true;
                movementSpeed = 10f;
                break;
            case 4: //4; It will have a curve, at a random speed
                angularCurve = true;
                movementSpeed = Random.Range(1f, 5f)*10f;
                break;
        }
        Arigidbody.velocity = new Vector2(Mathf.Cos(angle * Mathf.Deg2Rad), Mathf.Sin(angle * Mathf.Deg2Rad) * movementSpeed); //Convert the degrees to radians, set that in a Vector2, and times it by the
    } //movement speed to get the velocity and direction

    void FixedUpdate()
    {
        playerPositionX = GameObject.Find("player").transform.position.x; //Keep finding the player, so that they don't spawn too far away
        playerPositionY = GameObject.Find("player").transform.position.y; //^
        if (angularCurve) //If it's supposed to have a curve, then run the coroutine for it
        {
            StartCoroutine(RandomSpin());
        }
        if (Vector2.Distance(transform.position, Camera.main.transform.position) > 10) //If they're too far away from the main camera, it will despawn and restart the entire process
            Start();
        if (Vector2.Distance(transform.position, Camera.main.transform.position) < -10)
            Start();
    }

    IEnumerator RandomSpin()
    {
        yield return new WaitForSeconds(1f); //After a second, it will increase the curve a bit - didn't mess around with the curve, found the game hard enough as is
        spin += 0.5f;
        Arigidbody.MoveRotation(angle + spin); //Set the rotation of the astroid to be it's current angle with a slight increase - they will always curve towards you
    }
}
