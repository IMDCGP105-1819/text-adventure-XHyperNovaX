using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class UserControls : MonoBehaviour
{
    public float movementSpeed = 5f; //Multiplier for movement - Not sure if it's the best value, but anything else felt too slow or too fast
    private Rigidbody2D rigidbody; //^albeit in saying that, I watch YouTube videos on double speed because they're too slow otherwise, so...
    private CircleCollider2D collider; //Renaming these for easier use
    private Renderer renderer;
    public bool invincibility = false; //Boolean value for when you've been hit and are invincible, so you don't lose all 3 lives instantly
    public float lives = 3f; //3 lives

    public GameObject[] allObjects; //A list of all the GameObjects

    void Start()
    {
        rigidbody = GetComponent<Rigidbody2D>();
        collider = GetComponent<CircleCollider2D>(); //Getting the components
        renderer = GetComponent<Renderer>();

        GameObject[] allObjects = FindObjectsOfType<GameObject>(); //Filling in the values of the list of GameObjects
    }
    
    void FixedUpdate()
    {
        switch (lives) //Shortened if/else if statement
        {
            case 0: //if "lives" is 0, then it loads the main menu
                SceneManager.LoadScene(0);
                break;
            case 1: //if "lives" is 1, then you are coloured red - so that the user knows to play safer
                renderer.material.color = Color.red;
                break;
            case 2: //if "lives" is 2, then you are coloured yellow - ^
                renderer.material.color = Color.yellow;
                break;
            case 3: //if "lives" is 3, then you are coloured green, you're safe
                renderer.material.color = Color.green;
                break;
        }

        float xDir = -1; //Constant scrolling to the left
        float yDir = Input.GetAxisRaw("Vertical")*2; //Your movement will be either 2, or -2, unless you use a joystick for easier control I guess - 1 was too slow to actually dodge, 5 was too fast
        Vector2 movement = new Vector2(xDir, yDir); //Save these values as a Vector2 to be used in the next line
        rigidbody.velocity = movement * movementSpeed; //Move the character up and left or down and left at 2 units per unit of time
    }
    
    public void OnTriggerEnter2D(Collider2D other) //If you collide with something else, then it will trigger the following
    { //isTrigger is set in the Inspector
        if (invincibility == false) //If you are invincible, you can carry on as you are, otherwise, the following-
        {
            if (other.gameObject.name != "player") //Find the colliding GameObject and teleport it elsewhere - the != "player" part was in case it detected itself, which isn't what I want
                other.gameObject.transform.SetPositionAndRotation(new Vector2(-1000, 0), Quaternion.Euler(0, 0, 0)); //Move the GameObject to -1000, 0; you'll never get there, and they despawn if too far
            StartCoroutine(InvincibilityDeactivation()); //Start the coroutine to deactivate your invincibility after 5 seconds
        }
    }

    IEnumerator InvincibilityDeactivation()
    {
        lives -= 1f; //You lose a life
        invincibility = true; //You become invincible so that you don't lose all your lives instantly
        yield return new WaitForSeconds(5f); //and after 5 seconds
        invincibility = false; //you become mortal once more
    }
}