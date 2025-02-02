package Step;

import Driver.BaseTest;
import com.thoughtworks.gauge.Step;
import lombok.extern.log4j.Log4j;
import model.ElementInfo;
import org.junit.Assert;
import org.junit.jupiter.api.Assertions;
import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.io.IOException;
import java.text.DecimalFormat;
import java.text.ParseException;
import java.time.Duration;
import static Driver.BaseTest.getFileList;
import static Driver.BaseTest.webDriver;
import static java.time.Duration.ofMillis;
import static java.time.Duration.ofSeconds;

@Log4j

public class StepImplementation{
    BaseTest baseTest;
    FluentWait<WebDriver> wait;


    public StepImplementation() throws IOException {
        baseTest = new BaseTest();
        String currentWorkingDir = System.getProperty("user.dir");
        baseTest.initMap(getFileList(currentWorkingDir + "/src/test/resources/elementValues"));
    }
    WebElement findElement(String key) {
        By infoParam = getElementInfoToBy(baseTest.findElementInfoByKey(key));
        WebDriverWait webDriverWait = new WebDriverWait(webDriver, Duration.ZERO.withSeconds(60));
        WebElement webElement = webDriverWait
                .until(ExpectedConditions.presenceOfElementLocated(infoParam));
        ((JavascriptExecutor) webDriver).executeScript(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})",
                webElement);
        return webElement;
    }

    public By getElementInfoToBy(ElementInfo elementInfo) {
        By by = null;
        if (elementInfo.getType().equals("css")) {
            by = By.cssSelector(elementInfo.getValue());
        } else if (elementInfo.getType().equals(("name"))) {
            by = By.name(elementInfo.getValue());
        } else if (elementInfo.getType().equals("id")) {
            by = By.id(elementInfo.getValue());
        } else if (elementInfo.getType().equals("xpath")) {
            by = By.xpath(elementInfo.getValue());
        } else if (elementInfo.getType().equals("linkText")) {
            by = By.linkText(elementInfo.getValue());
        } else if (elementInfo.getType().equals(("partialLinkText"))) {
            by = By.partialLinkText(elementInfo.getValue());
        }
        return by;
    }

    public void waitBySecond(long seconds) {
        try {
            Thread.sleep(seconds * 1000);
        } catch (Exception e) {
            e.printStackTrace();
        }
        log.info(seconds+ " saniye beklendi");
    }

    public void waitPage(){
        JavascriptExecutor js = (JavascriptExecutor) webDriver;

        boolean isPageLoaded = js.executeScript("return document.readyState").equals("complete");
        if (isPageLoaded){
            log.info("Sayfa yüklendi");
        }else {
            log.info("Sayfa yüklenmedi");
        }
    }

    public void clickElement(String key){
        findElement(key).click();
        log.info("Elemente tıklandı");
    }
    public void clearElement(String key){
        findElement(key).clear();
        log.info("Elementin Text alanı temizlendi");
    }

    public void sendKeyss(String key,String text){
        findElement(key).sendKeys(text);
        System.out.println("Elemente "+text+" değeri yazıldı");
    }

    public void acceptAlert(){
        wait.until(ExpectedConditions.alertIsPresent());
        webDriver.switchTo().alert().accept();
    }


    @Step("<key> elementine tikla")
    public void clickElements(String key) {
        clickElement(key);
        log.info(key+" elementine tıklanıldı");
    }

    @Step("Site uyarisi kabul edilir")
    public void acceptSiteAlert() {
        acceptAlert();
    }

    @Step("<key> elementininin input alanini temizle")
    public void clearElements(String key) {
        clearElement(key);
        log.info(key+" elementinin input alani temizlendi");
    }

    @Step("<saniye> saniye bekle")
    public void waitBySeconds(Long saniye) {
        waitBySecond(saniye);
        log.info(saniye+" saniye beklendi");
    }

    @Step("<key> elementinin texti <text> degerini iceriyor mu")
    public void textControl(String key, String text) {
        String actualText =findElement(key).getText();
        if (text.contains(actualText)){
            log.info(actualText+ " degeri " +text+ " degerini iceriyor");
        }
        else {
            Assert.fail(actualText+ " degeri " +text+ " degerini icermiyor");
        }
    }

    @Step("<key> elementine <text> yaz")
    public void sendkeys(String key,String text) {
        sendKeyss(key, text);
        log.info(key+ "elementine gonderilen text = "+text);
    }
    @Step("Suan ki url <url> degerini iceriyor mu")
    public void checkToUrl(String url){
        String actualUrl = webDriver.getCurrentUrl();
        if (actualUrl.contains(url)){
            log.info(actualUrl + " URL'i " +url+ "degerini içeriyor");
        }else {
            Assert.fail(actualUrl + " URL'i " +url+ "degerini içermiyor");
        }
    }

    @Step({"Verify <key> element is not visible in <x> seconds at most",
            "<key> elementinin gorunur olmadigini en fazla <x> saniye icinde dogrula"})
    public void verifyInvisibilityOfElement(String key, long seconds) {
        By infoParam = getElementInfoToBy(baseTest.findElementInfoByKey(key));
        WebDriverWait wait = new WebDriverWait(webDriver, Duration.ofSeconds(seconds));
        try {
            wait.until(ExpectedConditions.invisibilityOfElementLocated(infoParam));
            log.info(key + " elementinin gorunur olmadigi "+seconds+" saniye içinde dogrulandi.");
        } catch (TimeoutException ignored) {
            Assertions.fail(String.format("%s elementinin gorunur olmadigi dogrulanamadi!", key));
        }
    }

    @Step("<key> elementinin gorunur oldugunu en fazla <x> saniye icinde dogrula")
    public void verifyVisibilityOfElement(String key, long seconds) {
        try {
            Wait<WebDriver> wait = new FluentWait<>(webDriver).
                    withTimeout(ofSeconds(seconds)).
                    pollingEvery(ofMillis(500)).
                    ignoring(NotFoundException.class).ignoring(NoSuchElementException.class);
            wait.until(ExpectedConditions.presenceOfElementLocated(getElementInfoToBy(baseTest.findElementInfoByKey(key))));
            log.info(key + " elementinin gorunur oldugu "+seconds+" saniye içinde dogrulandi.");
        } catch (TimeoutException ignored) {
            Assertions.fail(String.format("%s elementinin gorunur oldugu dogrulanamadi!", key));
        }

    }
    String ilkdeger;
    @Step("<key> elementinin textini hafızaya kaydet")
    public void saveTheText(String key) {
        ilkdeger = findElement(key).getText();
        log.info("Hafızaya Alınan Değer = "+ilkdeger);
    }
    @Step("<key> elementinin textini hafizadaki text ile karşılaştır.")
    public void compareWithRecorder(String key) {
        String text = findElement(key).getText();
        log.info("Değer = "+text);
        if (text.contains(ilkdeger)){
            Assertions.fail("Para aktarım işlemi gerçekleştirilemedi");
        }else {
            log.info("Para aktarım işlemi başarı ile gerçekleştirildi");
        }
    }

    @Step("<key> elementindeki değer hafizadaki değer ve <deger> <islem> sonrasi esit mi")
    public void totalAmountIslemkontrol(String key, int deger,String islem) throws ParseException {
        DecimalFormat decimalFormat = new DecimalFormat("#,##0.00");
        String text = findElement(key).getText();
        log.info("Değer = "+text);
        double sondeger = Double.parseDouble(text.replace(",","").replace(".00",""));
        switch (islem){
            case "toplama":
                double num1= Double.parseDouble(ilkdeger.replace(",","").replace(".00",""));
                double result = num1+deger;
                if (sondeger==result){
                    log.info("Miktar = "+sondeger+" degeri ile eklenince sonuc = "+result);
                }else {
                    Assert.fail("Eşit değil çünkü Miktar = "+sondeger+" degeri ile eklenince sonuc = "+result);
                }
                break;
            case "cikarma":
                num1 = Double.parseDouble(ilkdeger.replace(",", "").replace(".00", ""));
                result = num1 - deger;
                if (sondeger==result){
                    log.info("Miktar = "+sondeger+" degeri ile çıkarılınca sonuc = "+result);
                }else {
                    Assert.fail("Eşit değil çünkü Miktar = "+sondeger+" degeri ile çıkarılınca sonuc = "+result);
                }
                break;
            default:
                Assertions.fail("Doğru işlem girilmedi");
        }
    }

    @Step("<key> elementine hafizadaki değerin ustune <deger> ekle")
    public void plusOneSaveTheTextSendKeys(String key, double deger) throws ParseException {
            double num1= Double.parseDouble(ilkdeger.replace(",","").replace(".00",""));
            double result = num1+deger;
            sendkeys(key, String.valueOf(result).replace(".0",""));
        }
    }


