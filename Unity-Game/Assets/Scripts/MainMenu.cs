using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{
    public void SceneChange (int selectedScene) //Values are set in the Inspector; 0 for the Main Menu, 1 for the Game, 2 for the How To Play tab.
    {
        SceneManager.LoadScene(selectedScene);
    }
}