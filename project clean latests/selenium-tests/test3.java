package finaltest;

import java.util.concurrent.TimeUnit;

import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.RemoteWebDriver;

public class test3 {
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

WebElement addFile = driver.findElement(By.name("username"));
addFile.sendKeys("finalTest");

WebElement addFile2 = driver.findElement(By.name("email"));
addFile2.sendKeys("finalTest@icloud.com");

WebElement addFile3 = driver.findElement(By.name("password"));
addFile3.sendKeys("BumiSignUp@5");

WebElement addFile4 = driver.findElement(By.name("confirmpassword"));
addFile4.sendKeys("BumiSignUp@5");

WebElement addFile5 = driver.findElement(By.name("signup"));
addFile5.click();



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
