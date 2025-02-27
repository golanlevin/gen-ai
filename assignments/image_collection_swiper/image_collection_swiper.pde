// Image Collection Swiper - An Image Dataset Editor
// By Cassie Scheirer & Golan Levin, CMU, 2019

import java.io.File;
import java.io.BufferedWriter;
import java.io.FileWriter;

StringList imageNames;
String folderOfImages;
String goodFolder;
String badFolder;
String logFolder;

boolean good = false;
boolean bad = false;
boolean next = false;
boolean newImg = true;

boolean loading = true;
boolean bLoaded = false;

PImage img;
int currImage = 0;

String currSession = "start";
StringList txtFiles;

String prevImgName;
String prevImgNewLocation;
boolean undo = false;
boolean undoBlock = false;
String dataPath;

void setup() {
  size(512, 512);
  textAlign(CENTER);

  // initialize data paths, arrays & lists
  dataPath = dataPath("");
  folderOfImages = dataPath + "/source_images";
  logFolder = dataPath + "/image_logs";
  goodFolder = dataPath + "/good";
  badFolder = dataPath + "/bad";

  imageNames = new StringList();
  txtFiles = new StringList();

  String[] allFiles = listFileNames(folderOfImages);
  String[] txtFiles = listFileNames(logFolder);

  // sort through given files in source_images and pick out the images
  for (int i = 0; i < allFiles.length; i++) {
    String file = allFiles[i];
    if ( file.toLowerCase().endsWith(".jpeg") || file.toLowerCase().endsWith(".bmp")
      || file.toLowerCase().endsWith(".jpg")  || file.toLowerCase().endsWith(".tif")
      || file.toLowerCase().endsWith(".png")  || file.toLowerCase().endsWith(".gif")) {
      imageNames.append(file);
    }
  }

  // on boot, determine the name of the output log
  // (month_day_year_session_session#)
  while (loading) {
    int session = 0;
    String D = nf(day(),2);
    String M = nf(month(),2);
    String Y = "" + year();

    // if there are logs already in the folder, make sure not to duplicate a name
    if (txtFiles.length > 0) {
      for (int i = 0; i < txtFiles.length; i++) {
        String sessionName = Y + "_" + M + "_" + D + "_session_" + str(session);

        if (txtFiles[i].equals(sessionName + ".txt")) {
          session += 1;
        }
      }
      currSession = Y + "_" + M + "_" + D + "_session_" + str(session);
    }
    // if there's aren't logs, it's the first one
    else {
      currSession = Y + "_" + M + "_" + D + "_session_" + str(session);
    }
    loading = false;
  }
}

void draw() {
  background(255);

  // stop when you've sorted all the images
  // black screen indicates you have finished
  if (currImage >= imageNames.size()) {
    background(0);
    fill(255,0,0); 
    textSize(60); 
    text("Done", 100,80); 
    return;
  }

  // undo last choice, return the sorted image to the original source_images folder
  if (undo == true) {
    currImage -= 1;
    undo = false;
    undoBlock = true;

    File file = new File(prevImgNewLocation + "/" + prevImgName);
    file.renameTo(new File(folderOfImages + "/" + prevImgName));
  }

  // load image onto canvas
  String imgString = imageNames.get(currImage);
  if (!bLoaded) {
    img = loadImage(folderOfImages + "/" + imgString);
    bLoaded = true;
  }


  // scale to fit canvas
  float resizeFactorW = round(float(width)/img.width * 100);
  float resizeFactorH = round(float(height)/img.height * 100);
  // image(img, 0, 0, img.width, img.height);


  if (img.width > 0 && img.height > 0) {
    if (img.width > img.height || img.width == img.height) {
      img.resize(int((resizeFactorW/100)*img.width), 0);
      image(img, 0, 0);
    } else {
      img.resize(0, int((resizeFactorH/100)*img.height));
      image(img, 0, 0);
    }
  }

  // print image data
  if (newImg) {
    newImg = false;
    println("Current Image: " + currImage + " - " + imgString);
  }

  // moving images between folders
  if (next == true) {
    // if a bad photo, write -1 on the data log and move the image from source_images to bad
    if (bad == true) {
      String data = imgString + "\t" + "-1";
      appendTextToFile(logFolder + "/" + currSession + ".txt", data);
      File file = new File(folderOfImages + "/" + imgString);
      file.renameTo(new File(badFolder + "/" + imgString));
      prevImgName = imgString;
      prevImgNewLocation = badFolder;
    }
    // if a good photo, log 1 and move to good
    else if (good == true) {
      String data = imgString + "\t" + "1";
      appendTextToFile(logFolder + "/" + currSession + ".txt", data);
      File file = new File(folderOfImages + "/" + imgString);
      file.renameTo(new File(goodFolder + "/" + imgString));
      prevImgName = imgString;
      prevImgNewLocation = goodFolder;
    }

    // increase image counter, reset variables
    currImage += 1;
    next = false;
    good = false;
    bad = false;
    undoBlock = false;
    newImg = true;
    bLoaded = false;
  }
}

void keyPressed() {
  if (key == CODED) {
    if (keyCode == LEFT) {
      bad = true;
      next = true;
    } else if (keyCode == RIGHT) {
      good = true;
      next = true;
    } else if (keyCode == UP) {
      if (!undoBlock) {
        undo = true;
      }
    }
  }
}

// given a folder of files, return an array of all the names of the files
String[] listFileNames(String dir) {
  File file = new File(dir);
  if (file.isDirectory()) {
    String names[] = file.list();
    return names;
  } else {
    return null;
  }
}

// given txt file, append given text
void appendTextToFile(String filename, String text) {
  File f = new File(dataPath(filename));
  try {
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(f, true)));
    out.println(text);
    out.close();
  }
  catch (IOException e) {
    e.printStackTrace();
  }
}
