package finaltest;

import java.util.concurrent.TimeUnit;

import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import static org.junit.Assert.assertTrue; 

public class test2 {

	private static RemoteWebDriver driver;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.setProperty("webdriver.chrome.driver", "C:\\Apache24\\htdocs\\Work\\chromedriver.exe");
		driver = new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
		
		driver.get("http://127.0.0.1:3030");
		try {
			Thread.sleep(2000);
		} catch (InterruptedException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}

WebElement addFile = driver.findElement(By.name("transcript"));
addFile.sendKeys("C:\\Apache24\\htdocs\\cs160\\Video-summary-project-master\\upload folder\\transcript\\transcript.txt");

WebElement addFile2 = driver.findElement(By.name("dictionary"));
addFile2.sendKeys("C:\\Apache24\\htdocs\\cs160\\Video-summary-project-master\\upload folder\\dictionary\\dictionary.txt");

WebElement addFile3 = driver.findElement(By.name("submitbutton"));
addFile3.click();



try {
	Thread.sleep(2000);
} catch (InterruptedException e) {
	// TODO Auto-generated catch block
	e.printStackTrace();
}


if(driver.findElement(By.name("summaryVid")).isDisplayed()) {
	System.out.println("it worked!");
	Assert.assertTrue("File Uploaded", true);
}else {
	Assert.assertTrue("File not Uploaded", false);
}
driver.quit();
}
		
}


