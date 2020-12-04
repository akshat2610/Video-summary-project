package finaltest;

import java.util.concurrent.TimeUnit;

import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.RemoteWebDriver;

public class test4 {
	private static RemoteWebDriver driver;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.setProperty("webdriver.chrome.driver", "C:\\Apache24\\htdocs\\Work\\chromedriver.exe");
		driver = new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
		
		driver.get("http://127.0.0.1:5000");
		try {
			Thread.sleep(2000);
		} catch (InterruptedException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}

WebElement addFile = driver.findElement(By.name("loginusername"));
addFile.sendKeys("testing1");

WebElement addFile2 = driver.findElement(By.name("loginpassword"));
addFile2.sendKeys("BumiSignUp@1");

WebElement addFile3 = driver.findElement(By.name("signin"));
addFile3.click();



try {
	Thread.sleep(1000);
} catch (InterruptedException e) {
	// TODO Auto-generated catch block
	e.printStackTrace();
}


if(driver.findElement(By.name("transcript")).isDisplayed()) {
	System.out.println("it worked!");
	Assert.assertTrue("Sign up complete", true);
}else {
	Assert.assertTrue("Sign up failed", false);
}
driver.quit();
	}
}
