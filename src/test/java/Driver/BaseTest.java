package Driver;

import Step.StepImplementation;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import com.thoughtworks.gauge.AfterScenario;
import com.thoughtworks.gauge.BeforeScenario;

import io.github.bonigarcia.wdm.WebDriverManager;
import lombok.extern.log4j.Log4j;
import model.ElementInfo;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.safari.SafariDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Type;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;
import java.util.stream.Stream;

@Log4j

public class BaseTest {
    public static WebDriver webDriver;
    public String baseUrl;
    StepImplementation step;
    public String browser = "Chrome";
    public String url = "https://catchylabs-webclient.testinium.com/";
    ConcurrentMap<String, Object> elementMapList = new ConcurrentHashMap<>();
    public BaseTest() throws IOException {
    }
    @BeforeScenario
    public void setDriver() {

        switch (browser) {
            case "Chrome":
                ChromeOptions chromeOptions = new ChromeOptions();
                WebDriverManager.chromedriver().setup();
                webDriver = new ChromeDriver(chromeOptions);
                System.out.println("Chrome Tarayıcısı başlatıldı");
                baseUrl = "" + url + "";
                webDriver.get(baseUrl);
                webDriver.manage().deleteAllCookies();
                webDriver.manage().window().maximize();
                break;

            case "Firefox":
                WebDriverManager.firefoxdriver().setup();
                webDriver = new FirefoxDriver();
                System.out.println("Firefox tarayıcısı başlatıldı");
                baseUrl = "" + url + "";
                webDriver.navigate().to(baseUrl);
                webDriver.manage().deleteAllCookies();
                webDriver.manage().window().maximize();
                break;

            case "Safari":
                WebDriverManager.safaridriver().setup();
                webDriver = new SafariDriver();
                System.out.println("Safari tarayıcısı başlatıldı");
                baseUrl = "" + url + "";
                webDriver.navigate().to(baseUrl);
                webDriver.manage().deleteAllCookies();
                webDriver.manage().window().maximize();
                break;
        }

    }
    public void initMap(List<File> fileList) {
        elementMapList = new ConcurrentHashMap<>();
        Type elementType = new TypeToken<List<ElementInfo>>() {
        }.getType();
        Gson gson = new Gson();
        List<ElementInfo> elementInfoList = null;
        for (File file : fileList) {
            try {
                FileReader filez = new FileReader(file);
                elementInfoList = gson
                        .fromJson(new FileReader(file), elementType);
                elementInfoList.parallelStream()
                        .forEach(elementInfo -> elementMapList.put(elementInfo.getKey(), elementInfo));
                System.out.println(file.getName() + " Dosyasında " + elementInfoList.size() + " Adet element değeri bulundu.");
            } catch (FileNotFoundException e) {

            }
        }
    }

    public static List<File> getFileList(String directoryName) throws IOException {
        List<File> dirList = new ArrayList<>();
        try (Stream<Path> walkStream = Files.walk(Paths.get(directoryName))) {
            walkStream.filter(p -> p.toFile().isFile()).forEach(f -> {
                if (f.toString().endsWith(".json")) {
                    dirList.add(f.toFile());
                }
            });
        }
        return dirList;
    }

    @AfterScenario
    public void driverQuit(){
        log.info("Driver Kapatıldı");
        webDriver.quit();
    }
    public ElementInfo findElementInfoByKey(String key) {
        return (ElementInfo) elementMapList.get(key);
    }
}
